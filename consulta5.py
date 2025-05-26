from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from genera_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import or_ # Se usa para combinar múltiples condiciones con "OR" dentro de una consulta.
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


# Listar todas las reacciones de tipo "alegre", "enojado", "pensativo" que sean de usuarios que cuyos nombre no inicien con vocal.
reacciones_filtradas = session.query(Reaccion).join(Usuario).filter(
    # Filtra las reacciones que sean "alegre", "enojado" o "pensativo"
    Reaccion.emocion.in_(["alegre", "enojado", "pensativo"]),
    # Excluye los usuarios cuyos nombres comiencen con una vocal
    ~or_(
        Usuario.usuario.like("a%"),  # Nombres que comienzan con "a"
        Usuario.usuario.like("e%"),  # Nombres que comienzan con "e"
        Usuario.usuario.like("i%"),  # Nombres que comienzan con "i"
        Usuario.usuario.like("o%"),  # Nombres que comienzan con "o"
        Usuario.usuario.like("u%")   # Nombres que comienzan con "u"
    )
).all()

# Mostrar resultados
for reaccion in reacciones_filtradas:
    print(f"Usuario: {reaccion.usuario.usuario}, Publicación: {reaccion.publicacion.publicacion}, Emoción: {reaccion.emocion}")
