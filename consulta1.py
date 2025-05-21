from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import *
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


#Listar publicaciones de un usuario.

usuarios = session.query(Publicacion).join(Usuario).filter(Usuario.usuario.like("%Karen%")).all()  #usamos join para unir publicaciones con usuario y filtramos para especificar que usuario mostrar

for l in usuarios:
	print(f"{l.publicacion}") #recorremos para listar todas las publicaciones del usuario especificado