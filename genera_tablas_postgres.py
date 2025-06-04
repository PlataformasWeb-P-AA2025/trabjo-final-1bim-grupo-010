from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion_postgres import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)
    
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50), nullable=False)
    
    reacciones = relationship("Reaccion", back_populates="usuario")
    publicaciones = relationship("Publicacion", back_populates="autor")

    def __repr__(self):
        return f"Usuario: id={self.id} usuario={self.usuario}"

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    publicacion = Column(String(100))

    autor = relationship("Usuario", back_populates="publicaciones")
    reacciones = relationship("Reaccion", back_populates="publicacion")

    def __repr__(self):
        return f"Publicacion: autor={self.usuario_id} contenido={self.publicacion}"

class Reaccion(Base):
    __tablename__ = 'reaccion'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)
    emocion = Column(String(50))

    usuario = relationship("Usuario", back_populates="reacciones")
    publicacion = relationship("Publicacion", back_populates="reacciones")

    def __repr__(self):
        return f"Reaccion: usuario={self.usuario_id} publicacion={self.publicacion_id} emocion={self.emocion}"




Base.metadata.create_all(engine)
