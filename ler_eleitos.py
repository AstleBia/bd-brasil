import pandas as pd
import numpy as np
import requests

# Lê o arquivo CSV
eleitos = pd.read_csv("/Users/bia/Downloads/municipios_eleitos_ibge.csv")

# Seleciona e renomeia as colunas (equivalente ao SELECT com AS do SQL)
eleitos_selecionados = eleitos[[
    'codigo_ibge',
    'municipio',
    'estado',
    'prefeito_eleito',
    'partido_prefeito',
    'vice_prefeito_eleito',
    'partido_vice',
    'turno'
]].rename(columns={
    'codigo_ibge': 'id_municipio',
    'municipio': 'nome_municipio',
    'estado': 'sigla_uf'
})

# Converte id_municipio para string
eleitos_selecionados['id_municipio'] = eleitos_selecionados['id_municipio'].astype(str)

# Substitui NaN por None (para compatibilidade com JSON/APIs)
eleitos_selecionados = eleitos_selecionados.replace({np.nan: None})

# Converte para lista de dicionários
data = eleitos_selecionados.to_dict(orient='records')

batch_size = 10000
url = 'http://172.19.4.145:9000/dados-eleitorais/eleitos-2024'

print(f"Total: {len(data)} registros")

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

