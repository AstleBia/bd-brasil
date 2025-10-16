from sqlmodel import SQLModel, Field
    
class DadosEleicao2022 (SQLModel, table=True):
    __tablename__ = "dados_eleicao_2022"
    __table_args__ = {"schema": "dados_eleitorais"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    sigla_uf: str = Field(max_length=2)
    turno: int
    cargo: str = Field(max_length=20)
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
    sigla_uf: str = Field(max_length=2)
    turno: int
    cargo: str = Field(max_length=20)
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
    cargo: str = Field(max_length=20)
    nome_candidato: str = Field(max_length=100)
    partido: str = Field(max_length=10)
    total_votos: int

class ResultadosEleicao2024 (SQLModel, table=True):
    __tablename__ = "resultados_eleicao_2024"
    __table_args__ = {"schema": "dados_eleitorais"}
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    cargo: str = Field(max_length=20)
    nome_candidato: str = Field(max_length=100)
    partido: str = Field(max_length=10)
    total_votos: int


class Municipio(SQLModel, table=True):
    __tablename__ = "municipios"
    id: int | None = Field(default=None, primary_key=True)
    id_municipio: str = Field(max_length=7)
    nome: str = Field(max_length=50)
    sigla_uf: str = Field(max_length=2)