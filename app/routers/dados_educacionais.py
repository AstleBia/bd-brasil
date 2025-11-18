from fastapi import APIRouter
from sqlmodel import Session, select
from ..database import SessionDep
from ..models import Escolas, OfertaEducacional
from ..schemas import EscolasCreate, OfertaEducacionalCreate

router = APIRouter(prefix="/dados-educacionais", tags=["Dados Educacionais"])

@router.get("/escolas")
def read_escolas(session: SessionDep) -> list[Escolas]:
    dados = session.exec(select(Escolas)).all()
    return dados

@router.post("/escolas")
def create_escolas(dados: list[EscolasCreate] | EscolasCreate, session: SessionDep) -> dict:
    if isinstance(dados,list):
        novos_dados = [Escolas(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted":len(novos_dados)}
    else:
        novo_dado = Escolas(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado

@router.get("/oferta-educacional")
def read_oferta_educacional(session: SessionDep) -> list[OfertaEducacional]:
    dados = session.exec(select(OfertaEducacional)).all()
    return dados

@router.post("/oferta-educacional")
def create_oferta_educacional(dados: list[OfertaEducacionalCreate] | OfertaEducacionalCreate, session: SessionDep) -> dict:
    if isinstance(dados, list):
        novos_dados = [OfertaEducacional(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted": len(novos_dados)}
    else:
        novo_dado = OfertaEducacional(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado