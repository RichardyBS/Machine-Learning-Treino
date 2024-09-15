import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_data(file_path):
    data = pd.read_csv(file_path)

    print("Dados brutos:\n", data.head())

    X = data['Descricao_Problema']
    y = data['Peças']

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    print("\nClasses codificadas:", label_encoder.classes_)

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # Vetorizar os dados de treino e teste
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Verificar o balanceamento das classes
    unique_classes, counts = np.unique(y_train, return_counts=True)
    print("\nDistribuição das classes no conjunto de treino:", dict(zip(unique_classes, counts)))

    # Aplicar SMOTE somente se houver desequilíbrio
    smote = SMOTE(random_state=42, k_neighbors=3)  # Reduzido o número de vizinhos
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_tfidf, y_train)

    return X_train_resampled, X_test_tfidf, y_train_resampled, y_test, label_encoder, vectorizer
