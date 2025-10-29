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

class ProducaoAgricolaPermanenteCreate(BaseModel):
    id_municipio: str
    ano: int
    nome_produto: str
    area_destinada_colheita: int | None
    area_colhida: int | None
    quantidade_produzida: float | None
    rendimento_medio_producao: float | None
    valor_producao: float | None