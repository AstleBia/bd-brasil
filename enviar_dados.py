import basedosdados as bd
import json
import requests

query = """
SELECT id_municipio, turno, cargo, votos_validos, votos_brancos, votos_nulos, abstencoes, aptos AS total_eleitores
FROM basedosdados.br_tse_eleicoes.detalhes_votacao_municipio
WHERE ano = 2024 AND id_municipio IS NOT NULL;
"""

df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)


data = df.to_dict(orient='records')
r = requests.post('http://172.19.4.145:9000/dados-eleicao-2024', json=data)

#formatado = json.dumps(data, indent=2)
#print(formatado)
#print(data[0])
#print(df.dtypes)

print(r.status_code)