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
    cargo: str
    nome_candidato: str 
    partido: str
    total_votos: int

class ResultadosEleicao2024Create (BaseModel):
    id_municipio: str
    cargo: str
    nome_candidato: str
    partido: str
    total_votos: int

class MunicipioCreate (BaseModel):
    id_municipio: str
    nome: str
    sigla_uf: str
    nome_uf: str
    nome_regiao: str