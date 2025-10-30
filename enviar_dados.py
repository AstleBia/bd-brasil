import basedosdados as bd
import numpy as np
import requests

query = """
SELECT id_municipio, ano, produto AS nome_produto, area_destinada_colheita, area_colhida, quantidade_produzida, rendimento_medio_producao, valor_producao
FROM `basedosdados.br_ibge_pam.lavoura_permanente` 
WHERE ano>= 2010 AND (area_destinada_colheita IS NOT NULL OR area_colhida IS NOT NULL OR quantidade_produzida IS NOT NULL OR rendimento_medio_producao IS NOT NULL OR valor_producao IS NOT NULL);
"""


df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)


df = df.replace({np.nan: None})
data = df.to_dict(orient='records')

batch_size = 5000
url = 'http://172.19.4.145:9000/panorama-economico/producao-agricola-permanente'

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