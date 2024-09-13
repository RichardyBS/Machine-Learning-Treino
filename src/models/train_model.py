import sys
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))

from preprocess_data import preprocess_data

def train_model():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dataset.csv'))

    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(file_path)

    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    y_pred = model.predict(X_test_tfidf)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Acurácia: {accuracy * 100:.2f}%')

    model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.pkl')
    
    with open(model_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    
    with open(vectorizer_path, 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)
    
    print(f"Modelo salvo em: {model_path}")
    print(f"Vectorizer salvo em: {vectorizer_path}")

if __name__ == "__main__":
    train_model()
