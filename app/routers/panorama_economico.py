from fastapi import APIRouter
from sqlmodel import select
from ..database import SessionDep
from ..models import PibSetores
from ..schemas import PibSetoresCreate

router = APIRouter(prefix="/panorama-economico", tags=["Panorama Econômico"])

@router.get("/pib-setores")
def read_pib_setores(session: SessionDep) -> list[PibSetores]:
    dados = session.exec(select(PibSetores)).all()
    return dados

@router.post("/pib-setores")
def create_pib_setores(dados: list[PibSetoresCreate] | PibSetoresCreate, session: SessionDep) -> dict:
    if isinstance(dados,list):
        novos_dados = [PibSetores(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted":len(novos_dados)}
    else:
        novo_dado = PibSetores(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado