
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.database import Base


AutorLibro = Table('autor_libro', Base.metadata,
                   Column('id', Integer, primary_key=True,
                          autoincrement=True,),
                   Column('autor_id', Integer, ForeignKey(
                       'autores.id', ondelete="CASCADE")),
                   Column('libro_id', String, ForeignKey(
                       'libros.id', ondelete="CASCADE"))
                   )


class Libro(Base):
    __tablename__ = "libros"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    autores = relationship(
        "Autor",
        secondary=AutorLibro,
        back_populates="libros")


class Autor(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    libros = relationship(
        "Libro",
        secondary=AutorLibro,
        back_populates="autores")
