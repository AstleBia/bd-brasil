from fastapi import APIRouter
from sqlmodel import select
from ..database import SessionDep
from ..models import PibSetores, ProducaoAgricolaPermanente, ProducaoAgricolaTemporaria
from ..schemas import PibSetoresCreate, ProducaoAgricolaPermanenteCreate, ProducaoAgricolaTemporariaCreate

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
    
@router.get("/producao-agricola-permanente")
def read_producao_agricola_permanente(session: SessionDep) -> list[ProducaoAgricolaPermanente]:
    dados = session.exec(select(ProducaoAgricolaPermanente)).all()
    return dados

@router.post("/producao-agricola-permanente")
def create_producao_agricola_permanente(dados: list[ProducaoAgricolaPermanenteCreate] | ProducaoAgricolaPermanenteCreate, session: SessionDep) -> dict:
    if isinstance(dados, list):
        novos_dados = [ProducaoAgricolaPermanente(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted":len(novos_dados)}
    else:
        novo_dado = ProducaoAgricolaPermanente(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado
    
@router.get("/producao-agricola-temporaria")
def read_producao_agricola_temporaria(session: SessionDep) -> list[ProducaoAgricolaTemporaria]:
    dados = session.exec(select(ProducaoAgricolaTemporaria)).all()
    return dados

@router.post("/producao-agricola-temporaria")
def create_producao_agricola_temporaria(dados: list[ProducaoAgricolaTemporariaCreate] | ProducaoAgricolaTemporariaCreate, session: SessionDep) -> dict:
    if isinstance(dados, list):
        novos_dados = [ProducaoAgricolaTemporaria(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted":len(novos_dados)}
    else:
        novo_dado = ProducaoAgricolaTemporaria(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado