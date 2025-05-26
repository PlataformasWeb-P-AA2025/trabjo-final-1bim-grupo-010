from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from genera_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import func # Permite acceder a las funciones de agregación y otras funciones SQL directamente dentro de SQLAlchemy.

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener la cantidad de usuarios que han reaccionado al menos a una publicación
cantidad_usuarios_reaccionaron = session.query(func.count(Reaccion.usuario_id.distinct())).scalar() # Cuenta los usuarios distintos que han reaccionado.

# Mostrar el total de usuarios que han reaccionado
print(f"Usuarios que han reaccionado al menos una vez: {cantidad_usuarios_reaccionaron}")


