from fastapi import APIRouter
from sqlmodel import select
from ..database import SessionDep
from ..models import PibSetores, ProducaoAnimal, ProducaoAgricola, EfetivoPecuaria
from ..schemas import PibSetoresCreate, ProducaoAnimalCreate, ProducaoAgricolaCreate, EfetivoPecuariaCreate

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
    
    
@router.get("/producao-animal")
def read_producao_animal(session: SessionDep) -> list[ProducaoAnimal]:
    dados = session.exec(select(ProducaoAnimal)).all()
    return dados

@router.post("/producao-animal")
def create_producao_animal(dados: list[ProducaoAnimalCreate] | ProducaoAnimalCreate, session: SessionDep) -> dict:
    if isinstance(dados, list):
        novos_dados = [ProducaoAnimal(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted":len(novos_dados)}
    else:
        novo_dado = ProducaoAnimal(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado
    
@router.get("/producao-agricola")
def read_producao_agricola(session: SessionDep) -> list[ProducaoAgricola]:
    dados = session.exec(select(ProducaoAgricola)).all()
    return dados

@router.post("/producao-agricola")
def create_producao_agricola(dados: list[ProducaoAgricolaCreate] | ProducaoAgricolaCreate, session: SessionDep) -> dict:
    if isinstance(dados, list):
        novos_dados = [ProducaoAgricola(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted":len(novos_dados)}
    else:
        novo_dado = ProducaoAgricola(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado
    
@router.get("/efetivo-pecuaria")
def read_efetivo_pecuaria(session: SessionDep) -> list[EfetivoPecuaria]:
    dados = session.exec(select(EfetivoPecuaria)).all()
    return dados

@router.post("/efetivo-pecuaria")
def create_efetivo_pecuaria(dados: list[EfetivoPecuariaCreate] | EfetivoPecuariaCreate, session: SessionDep) -> dict:
    if isinstance(dados, list):
        novos_dados = [EfetivoPecuaria(**dado.model_dump()) for dado in dados]
        session.add_all(novos_dados)
        session.commit()
        return {"inserted": len(novos_dados)}
    else:
        novo_dado = EfetivoPecuaria(**dados.model_dump())
        session.add(novo_dado)
        session.commit()
        session.refresh(novo_dado)
        return novo_dado