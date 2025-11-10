from fastapi import APIRouter
from sqlmodel import Session, select
from ..database import SessionDep
from ..models import Escolas
from ..schemas import EscolasCreate

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