from sqlmodel import SQLModel, Field
    
class DadosEleicao2022 (SQLModel, table=True):
    __tablename__ = "dados_eleicao_2022"
    __table_args__ = {"schema": "dados_eleitorais"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    turno: int
    cargo: str = Field(max_length=35)
    votos_validos: int
    votos_brancos: int
    votos_nulos: int
    abstencoes: int
    total_eleitores: int

class DadosEleicao2024 (SQLModel, table=True):
    __tablename__ = "dados_eleicao_2024"
    __table_args__ = {"schema": "dados_eleitorais"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    turno: int
    cargo: str = Field(max_length=35)
    votos_validos: int
    votos_brancos: int
    votos_nulos: int
    abstencoes: int
    total_eleitores: int

class ResultadosEleicao2022 (SQLModel, table=True):
    __tablename__ = "resultados_eleicao_2022"
    __table_args__ = {"schema": "dados_eleitorais"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    turno: int
    cargo: str = Field(max_length=35)
    nome_candidato: str = Field(max_length=100)
    nome_urna: str = Field(max_length=100)
    sigla_partido: str = Field(max_length=30)
    resultado: str = Field(max_length=30)
    total_votos: int

class ResultadosEleicao2024 (SQLModel, table=True):
    __tablename__ = "resultados_eleicao_2024"
    __table_args__ = {"schema": "dados_eleitorais"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    turno: int
    cargo: str = Field(max_length=35)
    nome_candidato: str = Field(max_length=100)
    nome_urna: str = Field(max_length=100)
    sigla_partido: str = Field(max_length=30)
    resultado: str = Field(max_length=30)
    total_votos: int


class Municipio(SQLModel, table=True):
    __tablename__ = "municipios"
    id_municipio: str = Field(max_length=7, primary_key=True)
    nome: str = Field(max_length=50)
    sigla_uf: str = Field(max_length=2)
    nome_uf: str = Field(max_length=30)
    nome_regiao: str = Field(max_length=30)


class PibSetores(SQLModel, table=True):
    __tablename__ = "pib_setores"
    __table_args__ = {"schema": "panorama_economico"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    ano: int
    pib_total: int
    pib_per_capita: float
    va_agropecuaria: int
    va_industria: int
    va_servicos: int
    participacao_agropecuaria: float
    participacao_industria: float
    participacao_servicos: float
    setor_predominante: str = Field(max_length=15)