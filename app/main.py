from fastapi import FastAPI

from app.schemas import Libro, Respuesta
from app.routers import libros

app = FastAPI()


@app.get("/")
def get_message() -> Respuesta:
    return Respuesta(age=20, name="Juan")

app.include_router(libros.router)