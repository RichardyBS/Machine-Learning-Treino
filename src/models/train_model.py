import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
import joblib

def train_model(file_path):
    # Carregar dados
    df = pd.read_csv(file_path)
    print(f"Data loaded. Number of rows: {len(df)}")
    print(f"Columns in the dataframe: {df.columns.tolist()}")

    # Ajustar os nomes das colunas para correspondam ao que está no CSV
    if 'Descrição_Problema' not in df.columns or 'Sintomas' not in df.columns or 'Peças' not in df.columns:
        raise KeyError("O DataFrame não contém as colunas esperadas. Verifique o arquivo CSV.")

    # Preparar dados
    X = df['Descrição_Problema']
    y = df['Peças']  # Ajuste isso de acordo com o que você deseja prever

    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vetorização dos dados
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Modelos e Grid Search
    models = {
        'Naive Bayes': MultinomialNB(),
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'SVM': LinearSVC()
    }

    param_grids = {
        'Naive Bayes': {
            'alpha': [0.1, 0.5, 1.0, 2.0],
            'fit_prior': [True, False]
        },
        'Logistic Regression': {
            'C': [0.1, 1.0, 10.0],
            'solver': ['liblinear', 'saga']
        },
        'SVM': {
            'C': [0.1, 1.0, 10.0],
            'max_iter': [1000, 2000]
        }
    }

    for model_name, model in models.items():
        print(f"\nTraining {model_name}")
        param_grid = param_grids[model_name]
        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
        grid_search.fit(X_train_tfidf, y_train)

        # Melhor modelo encontrado
        best_model = grid_search.best_estimator_
        print(f"Best parameters for {model_name}: {grid_search.best_params_}")

        # Avaliação do modelo
        y_pred = best_model.predict(X_test_tfidf)
        print(f"Accuracy for {model_name}: {accuracy_score(y_test, y_pred)}")
        print(f"Classification Report for {model_name}:")
        print(classification_report(y_test, y_pred))

        # Salvar modelo e vetorizador
        joblib.dump(best_model, f'src/models/{model_name.lower().replace(" ", "_")}_model.pkl')
        joblib.dump(vectorizer, 'src/models/vectorizer.pkl')
        print(f"Model and vectorizer for {model_name} saved.")

    # Estatísticas dos dados
    print("\nData statistics:")
    print(df['Peças'].value_counts())
    print(df.isnull().sum())

if __name__ == "__main__":
    train_model('src/data/preprocessed_data.csv')
