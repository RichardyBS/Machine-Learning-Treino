import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Caminhos dos arquivos
model_path = 'path/to/trained_model.pkl'
vectorizer_path = 'path/to/tfidf_vectorizer.pkl'

# Função para carregar o modelo e o vectorizer
def load_model_and_vectorizer(model_path, vectorizer_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(vectorizer_path, 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Função para fazer previsões
def make_predictions(model, vectorizer, new_data):
    # Transformar os dados novos usando o vectorizer
    X_new = vectorizer.transform(new_data)
    # Fazer previsões com o modelo
    predictions = model.predict(X_new)
    return predictions

# Exemplo de uso
if __name__ == "__main__":
    # Carregar o modelo e o vectorizer
    model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)
    
    # Dados novos para prever (exemplo com um dataframe)
    new_data = [
        "Carro não liga",
        "Ruído estranho ao frear"
    ]
    
    # Fazer previsões
    predictions = make_predictions(model, vectorizer, new_data)
    
    # Mostrar os resultados
    for text, prediction in zip(new_data, predictions):
        print(f"Texto: {text}\nPrevisão: {prediction}\n")
