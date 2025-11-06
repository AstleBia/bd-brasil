import pandas as pd

# Lê o arquivo CSV
escolas = pd.read_csv("lista_escolas_inep.csv")

# Seleciona e renomeia as colunas (equivalente ao SELECT com AS do SQL)
escolas_selecionadas = escolas[[
    'Escola',
    'Código INEP',
    'UF',
    'Município',
    'Dependência Administrativa',
    'Categoria Escola Privada',
    'Conveniada Poder Público'
]].rename(columns={
    'Código INEP': 'cod_inep',
    'Município': 'municipio',
    'Dependência Administrativa': 'dep_adm',
    'Categoria Escola Privada': 'cat_escola_privada',
    'Conveniada Poder Público': 'conveniada_poder_publico'
})

# Aplica o filtro WHERE dep_adm != 'Privada'
escolas_selecionadas = escolas_selecionadas[escolas_selecionadas['dep_adm'] != 'Privada']

# Exibe informações sobre o DataFrame resultante
print("Shape:", escolas_selecionadas.shape)
print("\nPrimeiras linhas:")
print(escolas_selecionadas.head())
print("\nInformações das colunas:")
print(escolas_selecionadas.info())