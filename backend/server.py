# backend/server.py

from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    user_input = request.json.get('message')
    # Aqui você deve integrar com seu modelo e ChatGPT
    response = handle_user_input(user_input)
    return jsonify({'response': response})

def handle_user_input(user_input):
    # Simule uma resposta para testes
    # Aqui você pode integrar com o seu modelo de ML e ChatGPT
    # Exemplo simples:
    return f"Resposta simulada para: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
