from fastapi import FastAPI  
from .routers import dados_eleitorais, panorama_economico  
  
app = FastAPI()  
  
app.include_router(dados_eleitorais.router)  
app.include_router(panorama_economico.router) 
