from fastapi import APIRouter , HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
ruta = APIRouter(
    prefix="/api/tickets",
    tags=["tickets"])

class Entrada(BaseModel):
    estado:str = Field(...,)
    prioridad:str = Field(...,)
    fecha:str = Field(...,)

class Salida(BaseModel):
    id:int = Field()
    descripcion: Optional[str]= Field()
    prioridad:Optional[str] = Field()
    estado: Optional[str]= Field()

@ruta.post(
    "/",
    response_model = Salida,
    status_code = status.HTTP_201_CREATED,
    summary = "crear un ticket "
) 
def crear_ticket(t):
    print()