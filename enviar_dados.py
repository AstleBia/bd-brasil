import basedosdados as bd
import numpy as np
import requests

query = """
SELECT 
    id_municipio, 
    ano, 
    CASE WHEN rede = '1' THEN 'FEDERAL' WHEN rede = '2' THEN 'ESTADUAL' WHEN rede = '3' THEN 'MUNICIPAL' END AS rede, 
    COALESCE(SUM(quantidade_matricula_infantil), 0) AS estudantes_infantil, 
    COALESCE(SUM(quantidade_matricula_fundamental), 0) AS estudantes_fundamental, 
    COALESCE(SUM(quantidade_matricula_medio), 0) AS estudantes_medio,
    COALESCE(SUM(quantidade_matricula_profissional), 0) AS estudantes_profissional,
    COALESCE(SUM(quantidade_matricula_eja), 0) AS estudantes_eja, 
    COALESCE(SUM(quantidade_docente_infantil), 0) AS docentes_infantil, 
    COALESCE(SUM(quantidade_docente_fundamental), 0) AS docentes_fundamental, 
    COALESCE(SUM(quantidade_docente_medio), 0) AS docentes_medio,
    COALESCE(SUM(quantidade_docente_profissional), 0) AS docentes_profissional,
    COALESCE(SUM(quantidade_docente_eja), 0) AS docentes_eja, 
    COUNTIF(etapa_ensino_infantil = 1) AS escolas_infantil, 
    COUNTIF(etapa_ensino_fundamental = 1) AS escolas_fundamental, 
    COUNTIF(etapa_ensino_medio = 1) AS escolas_medio, 
    COUNTIF(etapa_ensino_profissional = 1) AS escolas_profissional, 
    COUNTIF(etapa_ensino_eja = 1) AS escolas_eja
FROM `basedosdados.br_inep_censo_escolar.escola` 
WHERE ano >= 2010 AND rede != '4'
GROUP BY ano, id_municipio, rede;
"""


df = bd.read_sql (
    query=query,
    billing_project_id='dados-eleitorais-474712'
)


df = df.replace({np.nan: None})
data = df.to_dict(orient='records')

batch_size = 10000
url = 'http://172.19.4.145:9000/dados-educacionais/oferta-educacional'

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