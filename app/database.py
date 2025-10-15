from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True, pool_size=20, max_overflow=40)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]