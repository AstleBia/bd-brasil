import pandas as pd
import numpy as np

# Caminho do arquivo CSV
arquivo_csv = '/Users/bia/Documents/Facilit/dados-enem/microdados_enem_2010/DADOS/MICRODADOS_ENEM_2010.csv'

print("Lendo arquivo CSV...")
# Ler o arquivo CSV com encoding apropriado
df = pd.read_csv(
    arquivo_csv,
    sep=';',  # Microdados do ENEM geralmente usam ponto e vírgula como separador
    encoding='latin-1',  # Encoding comum para arquivos do INEP
    low_memory=False
)

print(f"Total de registros lidos: {len(df)}")
print(f"Colunas disponíveis: {df.columns.tolist()}")

# Colunas de interesse
colunas_interesse = [
    'CO_MUNICIPIO_ESC',  # Código do município
    'TP_DEPENDENCIA_ADM_ESC',  # Tipo de dependência administrativa
    'NU_NOTA_CN',  # Nota Ciências da Natureza
    'NU_NOTA_CH',  # Nota Ciências Humanas
    'NU_NOTA_LC',  # Nota Linguagens e Códigos
    'NU_NOTA_MT',  # Nota Matemática
    'NU_NOTA_REDACAO'  # Nota Redação
]

# Selecionar apenas as colunas de interesse
df_filtrado = df[colunas_interesse].copy()

# Filtrar apenas redes públicas (1=Federal, 2=Estadual, 3=Municipal)
# Excluir 4=Privada
df_filtrado = df_filtrado[df_filtrado['TP_DEPENDENCIA_ADM_ESC'].isin([1, 2, 3])].copy()

print(f"Total de registros após filtrar apenas redes públicas: {len(df_filtrado)}")

# Converter colunas de notas para numérico (substituir valores inválidos por NaN)
colunas_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
for coluna in colunas_notas:
    df_filtrado[coluna] = pd.to_numeric(df_filtrado[coluna], errors='coerce')

print("\nCalculando médias por município e tipo de dependência administrativa...")

# Agrupar por município e tipo de dependência administrativa, calculando a média das notas
df_agrupado = df_filtrado.groupby(
    ['CO_MUNICIPIO_ESC', 'TP_DEPENDENCIA_ADM_ESC'],
    as_index=False
).agg({
    'NU_NOTA_CN': 'mean',
    'NU_NOTA_CH': 'mean',
    'NU_NOTA_LC': 'mean',
    'NU_NOTA_MT': 'mean',
    'NU_NOTA_REDACAO': 'mean'
})

# Renomear colunas para deixar mais claro que são médias
df_agrupado.columns = [
    'id_municipio',
    'rede',
    'media_ciencias_natureza',
    'media_ciencias_humanas',
    'media_linguagens_codigos',
    'media_matematica',
    'media_redacao'
]

# Converter id_municipio para string
df_agrupado['id_municipio'] = df_agrupado['id_municipio'].astype(int).astype(str)

# Mapear valores numéricos de rede para texto
mapa_rede = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal'
}
df_agrupado['rede'] = df_agrupado['rede'].map(mapa_rede)

# Adicionar coluna ano com valor 2023
df_agrupado['ano'] = 2010

# Reordenar colunas para colocar 'ano' depois de 'rede'
colunas_ordenadas = ['id_municipio', 'ano', 'rede', 'media_ciencias_natureza', 
                      'media_ciencias_humanas', 'media_linguagens_codigos', 
                      'media_matematica', 'media_redacao']
df_agrupado = df_agrupado[colunas_ordenadas]

# Arredondar as médias para 2 casas decimais
colunas_medias = ['media_ciencias_natureza', 'media_ciencias_humanas', 
                   'media_linguagens_codigos', 'media_matematica', 'media_redacao']
df_agrupado[colunas_medias] = df_agrupado[colunas_medias].round(2)

print(f"\nTotal de grupos (município + dependência administrativa): {len(df_agrupado)}")
print("\nPrimeiras linhas do resultado:")
print(df_agrupado.head(10))

# Salvar resultado em CSV
arquivo_saida = 'medias_enem_2010_por_municipio.csv'
df_agrupado.to_csv(arquivo_saida, index=False, encoding='utf-8-sig')
print(f"\nResultado salvo em: {arquivo_saida}")

# Estatísticas gerais
print("\n" + "="*80)
print("ESTATÍSTICAS GERAIS")
print("="*80)
print(df_agrupado[colunas_medias].describe())

# Informações sobre tipos de dependência administrativa
print("\n" + "="*80)
print("DISTRIBUIÇÃO POR REDE DE ENSINO")
print("="*80)
redes = df_agrupado['rede'].value_counts()
print(redes)

