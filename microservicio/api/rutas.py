from fastapi import APIRouter , HTTPException, status
from pydantic import BaseModel, Field
from typing import List,Optional
from datetime import datetime
from microservicio.servicios import logicanegocio

ruta = APIRouter(
    prefix="/api/tickets",
    tags=["tickets"])

class Entrada(BaseModel):
    descripcion: Optional[str] = Field(None, example="Falla en login")
    prioridad: str = Field(..., example="alta")
    estado: str = Field(..., example="pendiente")
    fecha: Optional[datetime] = Field(None, example="2025-12-09T18:00:00")

class Salida(BaseModel):
    id: int = Field(..., description="ID único del ticket")

@ruta.post(
    "/",
    response_model = Salida,
    status_code = status.HTTP_201_CREATED,
    summary = "crear un ticket "
) 
def crear(ticket:Entrada):
    try:
        creado = logicanegocio.crear( ticket.descripcion, ticket.prioridad, ticket.estado, ticket.fecha)
        return creado
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = str(e)
        )
    
@ruta.get(
    "/",
    response_model = List[Salida],
    status_code = status.HTTP_200_OK,
    summary = "lista los tickets"
)
def listar():
    try:
        return logicanegocio.listar()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "error al listar"
        )