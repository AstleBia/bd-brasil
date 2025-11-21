from pydantic import BaseModel
    
class DadosEleicao2022Create (BaseModel):
    id_municipio: str
    turno: int
    cargo: str
    votos_validos: int
    votos_brancos: int
    votos_nulos: int
    abstencoes: int
    total_eleitores: int

class DadosEleicao2024Create (BaseModel):
    id_municipio: str
    turno: int
    cargo: str
    votos_validos: int
    votos_brancos: int
    votos_nulos: int
    abstencoes: int
    total_eleitores: int

class ResultadosEleicao2022Create (BaseModel):
    id_municipio: str
    turno: int
    cargo: str
    nome_candidato: str 
    nome_urna: str
    sigla_partido: str
    resultado: str
    total_votos: int

class ResultadosEleicao2024Create (BaseModel):
    id_municipio: str
    turno: int
    cargo: str
    nome_candidato: str
    nome_urna: str
    sigla_partido: str
    resultado: str
    total_votos: int

class MunicipioCreate (BaseModel):
    id_municipio: str
    nome: str
    sigla_uf: str
    nome_uf: str
    nome_regiao: str


class PibSetoresCreate(BaseModel):
    id_municipio: str
    ano: int
    pib_total: int
    pib_per_capita: float
    va_agropecuaria: int
    va_industria: int
    va_servicos: int
    participacao_agropecuaria: float
    participacao_industria: float
    participacao_servicos: float

class ProducaoAnimalCreate(BaseModel):
    id_municipio: str
    ano: int
    tipo: str
    nome_produto: str
    quantidade: int
    unidade: str
    valor: int

class ProducaoAgricolaCreate(BaseModel):
    id_municipio: str
    ano: int
    tipo: str
    nome_produto: str
    area_destinada_colheita: int | None
    area_colhida: int | None
    quantidade_produzida: float | None
    rendimento_medio_producao: float | None
    valor_producao: float | None

class EfetivoPecuariaCreate(BaseModel):
    id_municipio: str
    ano: int
    tipo_rebanho: str
    quantidade: int

class EscolasCreate(BaseModel):
    codigo_inep: str
    nome_escola: str
    sigla_uf: str
    nome_municipio: str
    dependencia_adm: str
    etapas_ensino: str | None

class OfertaEducacionalCreate(BaseModel):
    id_municipio: str
    ano: int
    rede: str
    estudantes_infantil: int
    estudantes_fundamental: int
    estudantes_medio: int
    estudantes_profissional: int
    estudantes_eja: int
    docentes_infantil: int
    docentes_fundamental: int
    docentes_medio: int
    docentes_profissional: int
    docentes_eja: int
    escolas_infantil: int
    escolas_fundamental: int
    escolas_medio: int
    escolas_profissional: int
    escolas_eja: int

class IdebEscolaCreate(BaseModel):
    id_municipio: str
    ano: int
    id_escola: str
    rede: str
    ensino: str
    ideb: float