import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Configuração do caminho para os dados do NLTK
nltk.data.path.append('C:\\Users\\richa\\AppData\\Roaming\\nltk_data')

# Baixando recursos necessários
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

def preprocess_text(text):
    # Tokenização
    tokens = word_tokenize(text.lower())  # Convertendo para minúsculas para consistência
    # Remoção de tokens que não são alfabéticos
    tokens = [word for word in tokens if word.isalpha()]
    # Remoção de stopwords
    stop_words = set(stopwords.words('portuguese'))
    tokens = [word for word in tokens if word not in stop_words]
    # Lematização
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

def preprocess_data(file_path):
    # Carregar dados
    df = pd.read_csv(file_path)
    print(f"Data loaded. Number of rows: {len(df)}")
    print(f"Columns in the dataframe: {df.columns.tolist()}")
    
    # Aplicar pré-processamento
    if 'Descrição_Problema' in df.columns:
        df['Descrição_Problema'] = df['Descrição_Problema'].apply(preprocess_text)
    if 'Sintomas' in df.columns:
        df['Sintomas'] = df['Sintomas'].apply(preprocess_text)
    if 'Peças' in df.columns:
        df['Peças'] = df['Peças'].apply(preprocess_text)
    if 'Soluções' in df.columns:
        df['Soluções'] = df['Soluções'].apply(preprocess_text)
    
    # Salvar dados pré-processados
    df.to_csv('src/data/preprocessed_data.csv', index=False)
    print("Preprocessing completed and data saved to 'src/data/preprocessed_data.csv'.")

if __name__ == "__main__":
    preprocess_data('src/data/dataset.csv')
