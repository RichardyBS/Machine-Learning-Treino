import pandas as pd

# Carregar dados do CSV
csv_path = './src/data/dataset.csv'
data = pd.read_csv(csv_path)

# Imprimir os nomes das colunas para verificar
print(data.columns)
