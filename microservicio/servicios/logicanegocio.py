from typing import Optional
from microservicio.servicios import basedatos

def crear(descripcion,prioridad,estado,fecha):
    id = basedatos.crear(descripcion,prioridad,estado,fecha)
    ticket =  {
        "id":id,
        "descripcion":descripcion,
        "prioridad":prioridad,
        "estado": estado,
        "fecha":fecha
    }
    return ticket

def listar():
    try:
        tickets = basedatos.listar()
        return tickets
    except Exception as e:
        return []