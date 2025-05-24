from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import *
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


#Listar publicaciones de un usuario.

resultados = session.query(Reaccion.emocion, func.count(Reaccion.emocion))\
    .group_by(Reaccion.emocion).order_by(func.count(Reaccion.emocion).desc()).all()

for emocion, cantidad in resultados:
    print(f"{emocion}: {cantidad}") #recorremos para listar todas las publicaciones en las que Karen ha reaccionado