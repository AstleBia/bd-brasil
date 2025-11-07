import pandas as pd
import numpy as np

# Lê o arquivo CSV
escolas = pd.read_csv("lista_escolas_inep.csv")

# Seleciona e renomeia as colunas (equivalente ao SELECT com AS do SQL)
escolas_selecionadas = escolas[[
    'Código INEP',
    'Escola',
    'UF',
    'Município',
    'Dependência Administrativa'
]].rename(columns={
    'Código INEP': 'codigo_inep',
    'Escola': 'nome_escola',
    'UF': 'sigla_uf',
    'Município': 'nome_municipio',
    'Dependência Administrativa': 'dependencia_adm'
})

# Converte codigo_inep para string
escolas_selecionadas['codigo_inep'] = escolas_selecionadas['codigo_inep'].astype(str)

# Aplica o filtro WHERE dependencia_adm != 'Privada'
escolas_selecionadas = escolas_selecionadas[escolas_selecionadas['dependencia_adm'] != 'Privada']

# Substitui NaN por None (para compatibilidade com JSON/APIs)
escolas_selecionadas = escolas_selecionadas.replace({np.nan: None})

# Converte para lista de dicionários
data = escolas_selecionadas.to_dict(orient='records')

# Exibe informações
print("Total de escolas:", len(data))
print("\nPrimeiros 3 registros:")
for i, escola in enumerate(data[:3], 1):
    print(f"\n{i}. {escola}")

print(type(data[0]['codigo_inep']))