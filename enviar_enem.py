import pandas as pd
import numpy as np
import requests
import json

# Lê o arquivo CSV gerado pelo dados_enem.py
# Define id_municipio como string ao ler o CSV
enem_data = pd.read_csv("medias_enem_2010_por_municipio.csv", dtype={'id_municipio': str})

print(f"Colunas disponíveis: {enem_data.columns.tolist()}")
print(f"Primeiras linhas:\n{enem_data.head()}")
print(f"Tipos de dados:\n{enem_data.dtypes}")

# Garantir que id_municipio é string
enem_data['id_municipio'] = enem_data['id_municipio'].astype(str)

# Remover registros com valores nulos nas colunas de notas
# (não faz sentido ter registros de médias sem notas)
colunas_notas = ['media_ciencias_natureza', 'media_ciencias_humanas', 
                 'media_linguagens_codigos', 'media_matematica', 'media_redacao']

total_antes = len(enem_data)
enem_data = enem_data.dropna(subset=colunas_notas)
total_depois = len(enem_data)

print(f"\nRegistros removidos com notas nulas: {total_antes - total_depois}")
print(f"Registros válidos para envio: {total_depois}")

# Substitui NaN por None (para compatibilidade com JSON/APIs)
enem_data = enem_data.replace({np.nan: None})

# Converte para lista de dicionários
data = enem_data.to_dict(orient='records')

batch_size = 10000
url = 'http://172.19.4.145:9000/dados-educacionais/enem'

print(f"\nTotal: {len(data)} registros")

for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    r = requests.post(url, json=batch)

    if r.status_code == 200:
        print(f"✓ Lote {i//batch_size + 1}: {len(batch)} registros")
    else:
        print(f"✗ Erro lote {i//batch_size + 1}: {r.status_code}")
        print(r.text[:300])
        break

print("Concluído!")

