from sqlmodel import SQLModel, Field, Column
from sqlalchemy import BigInteger, Float
    
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
    pib_total: int = Field(sa_column=Column(BigInteger))
    pib_per_capita: float = Field(sa_column=Column(Float))
    va_agropecuaria: int = Field(sa_column=Column(BigInteger))
    va_industria: int = Field(sa_column=Column(BigInteger))
    va_servicos: int = Field(sa_column=Column(BigInteger))
    participacao_agropecuaria: float = Field(sa_column=Column(Float))
    participacao_industria: float = Field(sa_column=Column(Float))
    participacao_servicos: float = Field(sa_column=Column(Float))

class ProducaoAgricolaPermanente(SQLModel, table=True):
    __tablename__ = "producao_agricola_permanente"
    __table_args__ = {"schema": "panorama_economico"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    ano: int
    nome_produto: str = Field(max_length=50)
    area_destinada_colheita: int | None
    area_colhida: int | None
    quantidade_produzida: float | None
    rendimento_medio_producao: float | None
    valor_producao: float | None

class ProducaoAgricolaTemporaria(SQLModel, table=True):
    __tablename__ = "producao_agricola_temporaria"
    __table_args__ = {"schema": "panorama_economico"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    ano: int
    nome_produto: str = Field(max_length=50)
    area_destinada_colheita: int | None
    area_colhida: int | None
    quantidade_produzida: float | None
    rendimento_medio_producao: float | None
    valor_producao: float | None

class ProducaoAnimal(SQLModel, table=True):
    __tablename__ = "producao_animal"
    __table_args__ = {"schema": "panorama_economico"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    ano: int
    tipo: str = Field(max_length=15)
    nome_produto: str = Field(max_length=100)
    quantidade: int
    unidade: str = Field(max_length=25)
    valor: int