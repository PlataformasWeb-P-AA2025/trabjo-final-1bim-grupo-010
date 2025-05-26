from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import *
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Mostrar en qué publicaciones reaccionó un usuario.
# Función para obtener las publicaciones en las que reaccionó un usuario específico.
def obtener_publicaciones_reaccionadas(nombre_usuario):
    # Buscar el usuario en la base de datos por su nombre
    usuario = session.query(Usuario).filter_by(usuario=nombre_usuario).first()
    
    if usuario:
        # Recorrer todas las reacciones del usuario y mostrar la publicación y la emoción asociada
        for reaccion in usuario.reacciones:
            print(f"{reaccion.publicacion.publicacion} + {reaccion.emocion}")
    else:
        print("Usuario no encontrado.")  # Mensaje en caso de que el usuario no exista

# Uso de la función con un usuario específico
obtener_publicaciones_reaccionadas("Robert")

