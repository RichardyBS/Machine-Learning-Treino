import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

model_path = 'path/to/trained_model.pkl'
vectorizer_path = 'path/to/tfidf_vectorizer.pkl'

def load_model_and_vectorizer(model_path, vectorizer_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(vectorizer_path, 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

def make_predictions(model, vectorizer, new_data):
    X_new = vectorizer.transform([new_data])
    predictions = model.predict(X_new)
    return predictions

if __name__ == "__main__":
    model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)
    new_data = [
        "Carro não liga",
        "Ruído estranho ao frear"
    ]
    predictions = make_predictions(model, vectorizer, new_data)
    for text, prediction in zip(new_data, predictions):
        print(f"Texto: {text}\nPrevisão: {prediction}\n")
