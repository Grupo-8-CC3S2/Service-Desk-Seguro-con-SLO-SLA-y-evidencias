from fastapi import FastAPI
import uvicorn
from microservicio.api.rutas import ruta as ruta_api
from microservicio.servicios.basedatos import iniciar_bd

def obtener_app():
    app = FastAPI()
    app.include_router(ruta_api)
    @app.on_event("startup")
    def al_levantar():
        iniciar_bd()
    @app.on_event("shutdown")
    def al_apagar():
        print()
    return app

app = obtener_app()

if __name__=="__main__":
    uvicorn("microservicio.main:app",host="0.0.0.0",port=8000,reload=True)