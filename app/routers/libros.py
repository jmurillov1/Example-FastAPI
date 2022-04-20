from fastapi import APIRouter, HTTPException
# from app import database as db
# from app.models import LibroModel

from app import models, schemas
from app.methods.libros import create_libro_sql, get_libros_sql


router = APIRouter(
    prefix="/libros",
)

@router.get("/")
def get_libros() -> list[schemas.Libro]:
    return get_libros_sql()


@router.post("/")
def create_libro(libro: schemas.Libro) -> schemas.Libro:
    return create_libro_sql(libro)


@router.get("/{libro_id}")
def search_libro(libro_id: str) -> schemas.Libro:
    # for libro in libros:
    #     if libro.id == libro_id:
    #         return libro
    return HTTPException(status_code=404, detail="Libro not found")

@router.delete("/{libro_id}")
def delete_libro(libro_id: str) -> schemas.Libro:
    # for libro in libros:
    #     if libro.id == libro_id:
    #         libros.remove(libro)
    #         return libro
    return HTTPException(status_code=404, detail="Libro not found")

@router.put("/{libro_id}")
def update_libro(libro_id: str, updated_libro: schemas.Libro) -> schemas.Libro:
    # for libro in libros:
    #     if libro.id == libro_id:
    #         libro.name = updated_libro.name or libro.name
    #         libro.autor = updated_libro.autor or libro.autor
    #         libro.year = updated_libro.year or libro.year
    #         return libro
    return HTTPException(status_code=404, detail="Libro not found")