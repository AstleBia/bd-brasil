import basedosdados as bd
import json
import requests

query = """
SELECT pm.id_municipio, pm.ano, pm.pib AS pib_total,(pm.pib/pop.populacao) AS pib_per_capita ,pm.va_agropecuaria,pm.va_industria,pm.va_servicos, ROUND(pm.va_agropecuaria/pm.va * 100,2) AS participacao_agropecuaria, ROUND(pm.va_industria/pm.va * 100,2) AS participacao_industria, ROUND(pm.va_servicos/pm.va * 100,2) AS participacao_servicos 
FROM `basedosdados.br_ibge_pib.municipio` AS pm
INNER JOIN `basedosdados.br_ibge_populacao.municipio` AS pop ON pm.id_municipio = pop.id_municipio AND pm.ano = pop.ano
WHERE pm.ano>=2010;
"""



df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)



data = df.to_dict(orient='records')
batch_size = 5000
url = 'http://172.19.4.145:9000/panorama-economico/pib-setores'

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