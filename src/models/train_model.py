import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

def train_model(file_path):
    # Carregar dados
    df = pd.read_csv(file_path)
    
    # Preparar os dados para treinamento
    X = df['Pergunta']  # Perguntas dos usuários
    y = df['Categoria']  # Categorias dos problemas
    
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Vetorizar o texto
    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    
    # Treinar o modelo
    model = MultinomialNB()
    model.fit(X_train_vectorized, y_train)
    
    # Avaliar o modelo
    y_pred = model.predict(X_test_vectorized)
    print(f"Acurácia do modelo: {accuracy_score(y_test, y_pred)}")
    print("\nRelatório de classificação:")
    print(classification_report(y_test, y_pred))
    
    # Salvar o modelo e o vetorizador
    joblib.dump(model, 'src/models/trained_model.pkl')
    joblib.dump(vectorizer, 'src/models/vectorizer.pkl')
    
    return model, vectorizer

if __name__ == "__main__":
    train_model('src/data/dataset.csv')
