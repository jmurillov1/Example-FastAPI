from app import database as db
from sqlalchemy.exc import SQLAlchemyError

from app import models, schemas
from uuid import uuid4 as uuid


def get_libros_sql():
    try:
        libros = db.session.query(models.Libro).all()
        return libros
    except SQLAlchemyError as e:
        print(e)


def create_libro_sql(libro: schemas.Libro):
    try:
        lib = models.Libro(id=str(uuid()), name=libro.name, year=libro.year)
        for au in libro.autores:
            autor = models.Autor(id=au.id, name=au.name)
            lib.autores.append(autor)
        db.session.add(lib)
        db.session.commit()
        return schemas.Libro(id=lib.id, name=lib.name, year=lib.year, autores=lib.autores)
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
