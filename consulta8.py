from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from genera_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


# Listar los usuarios que han realizado publicaciones
usuarios_con_publicaciones = session.query(Usuario).join(Publicacion).distinct().all()
# Realiza una unión con la tabla Publicacion para traer solo usuarios que tengan publicaciones asociadas.
# Se asegura de que no haya usuarios repetidos, evitando que aparezcan varias veces si han realizado múltiples publicaciones.

# Mostrar los nombres de usuarios que han publicado algo
print("Usuarios con publicaciones:")
for usuario in usuarios_con_publicaciones:
    print(usuario.usuario)

