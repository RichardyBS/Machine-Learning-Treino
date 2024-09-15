from flask import Flask, request, jsonify, send_from_directory
import pickle
import pandas as pd
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
import google.generativeai as genai
import os

# Configure a chave da API do Gemini
genai.configure(api_key="AIzaSyADiEFwXSJqvmoigq7LUbrsQLoMoZXFSC4")  # Substitua pela sua chave API do Gemini

app = Flask(__name__, static_folder="../src/frontend", template_folder="../src/frontend")
CORS(app)

# Carregar o modelo e o vetorizador
model_path = 'C:/RichardyBS/Machine Learning/src/models/trained_model.pkl'
vectorizer_path = 'C:/RichardyBS/Machine Learning/src/models/tfidf_vectorizer.pkl'
csv_path = 'C:/RichardyBS/Machine Learning/src/data/dataset.csv'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Carregar dados do CSV
data = pd.read_csv(csv_path)

# Verificar colunas corretas
print("Available columns in DataFrame:", data.columns)

# Nomes das colunas
column_name_solution = 'Solucoes'
column_name_price = 'PrecoEstimado'

if column_name_solution in data.columns and column_name_price in data.columns:
    # Criar mapeamentos para soluções e preços
    index_to_solution = dict(zip(data.index, data[column_name_solution]))
    index_to_price = dict(zip(data.index, data[column_name_price]))
else:
    print(f"One or more required columns are missing.")
    index_to_solution = {}
    index_to_price = {}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory(app.static_folder, 'styles.css')

@app.route('/app.js')
def script():
    return send_from_directory(app.static_folder, 'app.js')

@app.route('/infer', methods=['POST'])
def infer():
    user_input = request.json.get('text')
    prediction = make_predictions(user_input)
    return jsonify(prediction)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    user_input = request.json.get('message')
    prediction = make_predictions(user_input)
    return jsonify(prediction)

def make_predictions(new_data):
    global model, vectorizer
    X_new = vectorizer.transform([new_data])
    predictions = model.predict(X_new)

    predicted_index = predictions[0]

    if predicted_index in index_to_solution:
        solution = index_to_solution[predicted_index]
        price_estimate = index_to_price.get(predicted_index, "Não disponível")

        # Use a API do Gemini para aprimorar a resposta
        gemini_response = get_gemini_response(new_data, solution)
        cost_estimate = f"Custo estimado: R${price_estimate},00"  # Ajuste para o formato necessário
    else:
        gemini_response = "Problema não reconhecido. Recomendamos que você visite uma oficina Porto Seguro para uma análise detalhada."
        cost_estimate = "Custo estimado: Não disponível"

    return {
        'problem': f"Problema identificado: {new_data}",
        'solution': solution,
        'cost': cost_estimate,
        'gemini_response': gemini_response
    }

def get_gemini_response(problem_description, solution):
    prompt = (  f"Um cliente relatou o seguinte problema no veículo: '{problem_description}'. "
                f"A solução sugerida pelo modelo é: '{solution}'. "
                "Forneça uma resposta detalhada, explicando o que pode estar causando o problema, "
                "a solução recomendada e um orçamento estimado para o reparo. "
                "Além disso, recomende que o cliente visite uma oficina Porto Seguro para uma análise detalhada.")

    model = genai.GenerativeModel("gemini-1.5-flash")
    
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=150,
                temperature=0.7,
            )
        )
        print("Gemini Response:", response.text)  # Log da resposta
        return response.text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Erro ao gerar resposta com a API Gemini."

if __name__ == '__main__':
    app.run(debug=True)
