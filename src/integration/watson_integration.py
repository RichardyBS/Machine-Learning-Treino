import pandas as pd
import requests
from flask import Flask, request, jsonify
from google.cloud import vertexai  # Import Vertex AI client library

# Configurações do Watson Assistant (unchanged)
api_key = 'G4f5EN3d74SMQOoOoBNVpeRzDOKNyoGwlYTk_ZtKHtFs'
url = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/8d610c74-bc8b-49ef-891f-cf77bf23cc48'
assistant_id = '2aeae012-ba8e-4f41-b742-45b755f0d3e0'

# Configure Vertex AI project and location (replace with your details)
project_id = "your-project-id"
location = "your-location"

# Create a Vertex AI client object
client = vertexai.EndpointServiceClient(location=location, project=project_id)

# Função para buscar o problema no dataset (unchanged)
def find_problem_in_dataset(user_input, file_path='./src/data/dataset.csv'):
    df = pd.read_csv(file_path)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['Descricao_Problema'])
    user_input_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_input_vector, X)
    best_match_index = similarities.argmax()
    problem_details = df.iloc[best_match_index]
    return problem_details

# Função para gerar resposta com Gemini
def generate_gemini_response(problem_details):
    problem = problem_details['Descricao_Problema']
    solution = problem_details['Solucoes']
    cost_estimate = "R$ 500,00"
    prompt = (f"O problema identificado é: {problem}. "
              f"Peça envolvida: {problem_details['pecas']}. "
              f"Os sintomas são: {problem_details['Sintomas']}. "
              f"A solução recomendada é: {solution}. "
              f"Quanto custa mais ou menos o conserto: {cost_estimate}. "
              "Recomendamos que você vá à oficina Porto Seguro mais próxima.")

    # Define the endpoint name (replace with your endpoint name)
    endpoint_name = "your-gemini-endpoint"

    # Use Vertex AI client to send request to Gemini endpoint
    response = client.predict(endpoint=endpoint_name, instances=[prompt])

    # Extract the generated text from the response
    generated_text = response.predictions[0]['text']

    return generated_text.strip()

# Função principal para processar e responder ao Watson Assistant
def process_and_respond(user_input):
    problem_details = find_problem_in_dataset(user_input)
    chatgpt_response = generate_gemini_response(problem_details)
    return chatgpt_response

# Função para enviar mensagem ao Watson Assistant (unchanged)
def send_message_to_watson(user_input):
    response = assistant.message_stateless(
        assistant_id=assistant_id,
        input={'text': user_input}
    ).get_result()
    return response['output']['generic'][0]['text']

# Rota para receber input e responder
@app.route('/diagnose', methods=['POST'])
def diagnose():
    user_input = request.json.get('message')
    response = process_and_respond(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)