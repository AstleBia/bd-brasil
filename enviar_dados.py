import basedosdados as bd
import json
import requests

query = """
SELECT resultados.turno, resultados.id_municipio, resultados.sigla_partido, candidatos.nome, resultados.resultado, resultados.votos
FROM basedosdados.br_tse_eleicoes.resultados_candidato AS resultados
INNER JOIN basedosdados.br_tse_eleicoes.candidatos AS candidatos ON resultados.titulo_eleitoral_candidato = candidatos.titulo_eleitoral
WHERE resultados.id_municipio IS NOT NULL AND resultados.ano = 2022
LIMIT 1000;
"""

df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)


data = df.to_dict(orient='records')
#r = requests.post('http://172.19.4.145:9000/dados-eleicao-2024', json=data)

#formatado = json.dumps(data, indent=2)
#print(formatado)
#print(data[0])
#print(df.dtypes)

print(json.dumps(data,indent=2))