from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from genera_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import func # Permite acceder a las funciones de agregación y otras funciones SQL directamente dentro de SQLAlchemy.

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


# Contar cuántas publicaciones existen en la base de datos
cantidad_publicaciones = session.query(func.count(Publicacion.id)).scalar() # Se usa para obtener un único valor de una consulta en lugar de una fila o lista de resultados.
# Si usamos .all() el resultado seria [(100,)] una lista con una tupla dentro.

# Mostrar el total
print(f"Total de publicaciones en la base de datos: {cantidad_publicaciones}")

