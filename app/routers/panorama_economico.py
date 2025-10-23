from fastapi import APIRouter
from ..database import SessionDep

router = APIRouter(prefix="/panorama-economico", tags=["Panorama Econômico"])
