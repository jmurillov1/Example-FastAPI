from pydantic import BaseModel


class Respuesta(BaseModel):
    name: str | None = None
    age: int | None = None

class Autor(BaseModel):
    id: int | None = None 
    name: str | None = None

    class Config:
        orm_mode = True


class Libro(BaseModel):
    id: str | None = None 
    name: str | None = None
    autores: list[Autor] = [] 
    year: int | None = None

    class Config:
        orm_mode = True
