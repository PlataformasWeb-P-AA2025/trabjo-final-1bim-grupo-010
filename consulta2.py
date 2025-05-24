from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import *
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


#Listar las reacciones a una publicación.

reacciones = session.query(Reaccion).join(Publicacion).filter(
    Publicacion.publicacion.like("%Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada.%")
).all()

emociones_vistas = set() #se crea un conjunto set vacio

for r in reacciones: #se recorre el objeto reacciones
    if r.emocion not in emociones_vistas: #se pregunta si la emocion ya paso y si no esta en el conjunto es porque todavia no se ha mostrado
        print(f"{r.publicacion.publicacion} + {r.emocion}")
        emociones_vistas.add(r.emocion) # se aniade la emocion en el conjunto para que no se vuelva a repetir en la siguiente iteracion