from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS
import google.generativeai as genai
import traceback

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyADiEFwXSJqvmoigq7LUbrsQLoMoZXFSC4")

try:
    model = joblib.load('src/models/trained_model.pkl')
    vectorizer = joblib.load('src/models/vectorizer.pkl')
    df = pd.read_csv('src/data/dataset.csv')
    print("Modelo, vetorizador e dataset carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar arquivos: {str(e)}")
    traceback.print_exc()

@app.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({'error': 'Mensagem não fornecida'}), 400

        print(f"Recebida mensagem: {user_input}")

        X_new = vectorizer.transform([user_input])
        
        predicted_category = model.predict(X_new)[0]
        print(f"Categoria prevista: {predicted_category}")

        relevant_data = df[df['Categoria'] == predicted_category].iloc[0]
        
        response_data = {
            'problem': user_input,
            'category': str(predicted_category),
            'solution': str(relevant_data['Solucoes']),
            'price_estimate': f"R$ {relevant_data['PrecoEstimado']:.2f}",
        }

        prompt = f"""
        Como mecânico experiente, continue este diálogo de diagnóstico automotivo:

        Cliente: "{user_input}"
        Mecânico: "{relevant_data['Solucoes']}"

        Forneça uma breve análise técnica (máximo 3 parágrafos) incluindo:
        1. Possíveis causas do problema
        2. Riscos imediatos
        3. Próximo passo recomendado

        Mantenha a resposta curta e focada no diagnóstico inicial.
        """
        
        model_ai = genai.GenerativeModel("gemini-1.5-flash")
        gemini_response = model_ai.generate_content(prompt)
        
        response_data['detailed_analysis'] = gemini_response.text
        
        print("Resposta gerada com sucesso!")
        return jsonify(response_data)

    except Exception as e:
        print(f"Erro no processamento: {str(e)}")
        traceback.print_exc()
        return jsonify({
            'error': 'Erro no processamento',
            'details': str(e)
        }), 500

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Diagnóstico Automotivo</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .container { max-width: 800px; margin: 0 auto; }
                input { padding: 10px; width: 300px; margin-right: 10px; }
                button { padding: 10px 20px; }
                #result { margin-top: 20px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Diagnóstico Automotivo</h2>
                <input type="text" id="problem" placeholder="Descreva o problema do carro">
                <button onclick="sendDiagnosis()">Diagnosticar</button>
                <div id="result"></div>

                <script>
                    async function sendDiagnosis() {
                        try {
                            const problem = document.getElementById('problem').value;
                            if (!problem) {
                                alert('Por favor, descreva o problema do carro');
                                return;
                            }

                            const response = await fetch('/diagnose', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify({ message: problem })
                            });

                            const data = await response.json();
                            
                            if (data.error) {
                                document.getElementById('result').innerHTML = `<p style="color: red">Erro: ${data.error}</p>`;
                                return;
                            }

                            document.getElementById('result').innerHTML = `
                                <h3>Categoria: ${data.category}</h3>
                                <p><strong>Solução:</strong> ${data.solution}</p>
                                <p><strong>Preço Estimado:</strong> ${data.price_estimate}</p>
                                <p><strong>Análise Detalhada:</strong></p>
                                <p>${data.detailed_analysis}</p>
                            `;
                        } catch (error) {
                            console.error('Erro:', error);
                            document.getElementById('result').innerHTML = `<p style="color: red">Erro ao processar a requisição</p>`;
                        }
                    }
                </script>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
