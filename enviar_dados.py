import basedosdados as bd
import json

query = """
SELECT id_municipio, turno, cargo, votos_validos, votos_brancos, votos_nulos, abstencoes, aptos
FROM basedosdados.br_tse_eleicoes.detalhes_votacao_municipio
WHERE ano = 2022
LIMIT 10;
"""

df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)
    
data = df.to_dict(orient='records')
formatado = json.dumps(data, indent=2)

print(formatado)