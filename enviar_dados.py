import basedosdados as bd
import json
import requests

query = """
SELECT resultados.id_municipio, resultados.turno, resultados.cargo, candidatos.nome AS nome_candidato, resultados.sigla_partido, resultados.resultado, resultados.votos AS total_votos
FROM basedosdados.br_tse_eleicoes.resultados_candidato_municipio AS resultados
INNER JOIN basedosdados.br_tse_eleicoes.candidatos AS candidatos ON resultados.titulo_eleitoral_candidato = candidatos.titulo_eleitoral AND resultados.ano = candidatos.ano
WHERE resultados.id_municipio IS NOT NULL AND resultados.ano = 2022;
"""

df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)


data = df.to_dict(orient='records')
r = requests.post('http://172.19.4.145:9000/resultados-eleicao-2022', json=data)

#formatado = json.dumps(data, indent=2)
#print(formatado)
#print(data[0])
#print(df.dtypes)

#print(json.dumps(data,indent=2))
print(r.status_code)