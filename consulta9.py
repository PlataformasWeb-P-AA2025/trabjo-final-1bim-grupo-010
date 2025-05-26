from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from genera_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import func # Permite acceder a las funciones de agregación y otras funciones SQL directamente dentro de SQLAlchemy.

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


# Obtener los usuarios con la mayor cantidad de publicaciones
# Con un join se une Usuario con Publicacion para contar las publicaciones de cada usuario.
# Luego se cuenta las publicaciones de cada usuario. func.count(Publicacion.id).label("num_publicaciones")
# Con el group by se agrupa por usuario para obtener un resultado por cada usuario.
# Por ultimo con el order by se ordena de mayor a menor según la cantidad de publicaciones.
usuarios_mas_activos = session.query(
    Usuario.usuario, func.count(Publicacion.id).label("num_publicaciones") # .label() se usa para asignar un nombre personalizado a una columna calculada en una consulta.
).join(Publicacion).group_by(Usuario.id).order_by(func.count(Publicacion.id).desc()).all()

# Mostrar resultados
print("Usuarios con más publicaciones:")
for usuario, num_publicaciones in usuarios_mas_activos:
    print(f"{usuario}: {num_publicaciones} publicaciones")

