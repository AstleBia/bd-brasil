import pandas as pd
import numpy as np
import requests
import json

# Lê o arquivo CSV
escolas = pd.read_csv("lista_escolas_inep.csv")

# Seleciona e renomeia as colunas (equivalente ao SELECT com AS do SQL)
escolas_selecionadas = escolas[[
    'Código INEP',
    'Escola',
    'UF',
    'Município',
    'Dependência Administrativa',
    'Etapas e Modalidade de Ensino Oferecidas'
]].rename(columns={
    'Código INEP': 'codigo_inep',
    'Escola': 'nome_escola',
    'UF': 'sigla_uf',
    'Município': 'nome_municipio',
    'Dependência Administrativa': 'dependencia_adm',
    'Etapas e Modalidade de Ensino Oferecidas': 'etapas'
})

# Converte codigo_inep para string
escolas_selecionadas['codigo_inep'] = escolas_selecionadas['codigo_inep'].astype(str)

# Aplica o filtro WHERE dependencia_adm != 'Privada'
escolas_selecionadas = escolas_selecionadas[escolas_selecionadas['dependencia_adm'] != 'Privada']

# Substitui NaN por None (para compatibilidade com JSON/APIs)
escolas_selecionadas = escolas_selecionadas.replace({np.nan: None})

# Converte para lista de dicionários
data = escolas_selecionadas.to_dict(orient='records')

batch_size = 10000
url = 'http://172.19.4.145:9000/dados-educacionais/escolas'

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