from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests
import json

# Configurações do Watson Assistant
api_key = 'G4f5EN3d74SMQOoOoBNVpeRzDOKNyoGwlYTk_ZtKHtFs'
url = 'https://api.au-syd.assistant.watson.cloud.ibm.com/instances/8d610c74-bc8b-49ef-891f-cf77bf23cc48'
assistant_id = '814ef62d-ee46-46a9-b65a-dd274898365c'
authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)
assistant.set_service_url(url)

def send_message_to_watson(user_input):
    response = assistant.message_stateless(
        assistant_id=assistant_id,
        input={'text': user_input}
    ).get_result()
    return response['output']['generic'][0]['text']

def process_and_respond(user_input):
    # Enviar para o modelo de Machine Learning
    ml_response = requests.post('URL_TO_YOUR_MODEL', json={'text': user_input})
    prediction = ml_response.json()
    
    # Gerar resposta usando ChatGPT
    chatgpt_response = generate_chatgpt_response(prediction)
    
    return chatgpt_response

def generate_chatgpt_response(prediction):
    # Aqui você pode integrar o modelo ChatGPT
    # Exemplo simplificado
    problem = prediction['problem']
    cost_estimate = prediction['cost']
    response = (f"Possível problema: {problem}. "
                f"Orçamento estimado para o reparo: {cost_estimate}. "
                "Recomendamos que você leve o veículo à oficina Porto Seguro mais próxima.")
    return response

def handle_user_input(user_input):
    response = process_and_respond(user_input)
    return response
