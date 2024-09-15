import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(file_path):
    # Carregar dados
    data = pd.read_csv(file_path)
    
    # Pré-processamento dos dados
    X = data['Descricao_Problema']
    y = data['pecas']  # Supondo que 'pecas' é a coluna que queremos prever

    # Codificação das labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Dividir em conjunto de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test, label_encoder

def train_model():
    file_path = 'C:/RichardyBS/Machine Learning/src/data/dataset.csv'

    # Pré-processar os dados
    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(file_path)

    # Vetorização
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Treinar o modelo
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    # Salvar o modelo e o vectorizer
    model_path = 'C:/RichardyBS/Machine Learning/src/models/trained_model.pkl'
    vectorizer_path = 'C:/RichardyBS/Machine Learning/src/models/tfidf_vectorizer.pkl'
    
    with open(model_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    
    with open(vectorizer_path, 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    print(f"Modelo salvo em: {model_path}")
    print(f"Vectorizer salvo em: {vectorizer_path}")

if __name__ == "__main__":
    train_model()
