from fastapi import FastAPI
from .database import SessionDep
from sqlmodel import select
from .models import *
from .schemas import *

app = FastAPI()


@app.get("/dados-eleicao-2022")
def read_dados_eleicao_2022(session:SessionDep) -> list[DadosEleicao2022]:
    dados = session.exec(select(DadosEleicao2022)).all()
    return dados

@app.get("/dados-eleicao-2024")
def read_dados_eleicao_2024(session:SessionDep) -> list[DadosEleicao2024]:
    dados = session.exec(select(DadosEleicao2024)).all()
    return dados

@app.get("/resultados-eleicao-2022")
def read_resultados_eleicao_2022(session:SessionDep) -> list[ResultadosEleicao2022]:
    dados = session.exec(select(ResultadosEleicao2022)).all()
    return dados

@app.get("/resultados-eleicao-2024")
def read_resultados_eleicao_2024(session:SessionDep) -> list[ResultadosEleicao2024]:
    dados = session.exec(select(ResultadosEleicao2024)).all()
    return dados

@app.post("/dados-eleicao-2022")
def create_dados_eleicao_2022(dado: DadosEleicao2022Create, session: SessionDep) -> DadosEleicao2022:
    novo_dado = DadosEleicao2022(**dado.model_dump())
    session.add(novo_dado)
    session.commit()
    session.refresh(novo_dado)
    return novo_dado

@app.post("/dados-eleicao-2024")
def create_dados_eleicao_2024(dado: DadosEleicao2024Create, session: SessionDep) -> DadosEleicao2024:
    novo_dado = DadosEleicao2024(**dado.model_dump())
    session.add(novo_dado)
    session.commit()
    session.refresh(novo_dado)
    return novo_dado

@app.post("/resultados-eleicao-2022")
def create_resultados_eleicao_2022(dado: ResultadosEleicao2022Create, session: SessionDep) -> ResultadosEleicao2022:
    novo_dado = ResultadosEleicao2022(**dado.model_dump())
    session.add(novo_dado)
    session.commit()
    session.refresh(novo_dado)
    return novo_dado

@app.post("/resultados-eleicao-2024")
def create_resultados_eleicao_2024(dado: ResultadosEleicao2024Create, session: SessionDep) -> ResultadosEleicao2024:
    novo_dado = ResultadosEleicao2024(**dado.model_dump())
    session.add(novo_dado)
    session.commit()
    session.refresh(novo_dado)
    return novo_dado

@app.get("/municipios")
def read_municipios(session: SessionDep) -> list[Municipio]:
    dados = session.exec(select(Municipio)).all()
    return dados

@app.post("/municipios")
def create_municipios(dado: MunicipioCreate, session: SessionDep) -> Municipio:
    novo_dado = Municipio(**dado.model_dump())
    session.add(novo_dado)
    session.commit()
    session.refresh(novo_dado)
    return novo_dado

@app.post("/municipios/batch")
def create_municipios(dados: list[MunicipioCreate], session: SessionDep) -> Municipio:
    novos_dados = [Municipio(**dado.model_dump()) for dado in dados]
    session.add_all(novos_dado)
    session.commit()
    return {"inserted": len(novos_dados)}