from fastapi import FastAPI

from app.routers import dados_educacionais  
from .routers import dados_eleitorais, panorama_economico  
  
app = FastAPI()  
  
app.include_router(dados_eleitorais.router)  
app.include_router(panorama_economico.router) 
app.include_router(dados_educacionais.router)
