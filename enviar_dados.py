import basedosdados as bd
import numpy as np
import requests

query = """
SELECT id_municipio, ano, 'aquicultura' AS tipo, produto AS nome_produto, quantidade, 'Quilogramas' AS unidade, valor
FROM `basedosdados.br_ibge_ppm.producao_aquicultura` 
WHERE ano>= 2010;
"""


df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)


df = df.replace({np.nan: None})
data = df.to_dict(orient='records')

batch_size = 5000
url = 'http://172.19.4.145:9000/panorama-economico/producao-animal'

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