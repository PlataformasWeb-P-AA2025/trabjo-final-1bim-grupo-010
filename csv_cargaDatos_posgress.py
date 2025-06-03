import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion_possgress import cadena_base_datos

# Conexión y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Cargar usuarios
with open('DATA/usuarios_red_x.csv', encoding='UTF-8') as archivo:
    lector = csv.DictReader(archivo, delimiter='|')
    for fila in lector:
        usuario = Usuario(usuario=fila['usuario'])
        session.add(usuario)

session.commit()  # Confirmamos para tener IDs asignados

# Cargar publicaciones
with open('DATA/usuarios_publicaciones.csv', encoding='UTF-8') as archivo:
    lector = csv.DictReader(archivo, delimiter='|')
    for fila in lector:
        usuario = session.query(Usuario).filter_by(usuario=fila['usuario']).first()
        if usuario:
            publicacion = Publicacion(usuario_id=usuario.id, publicacion=fila['publicacion'])
            session.add(publicacion)

session.commit()  # Confirmamos para tener ids de publicaciones asignados

# Cargar reacciones
with open('DATA/usuario_publicacion_emocion.csv', encoding='UTF-8') as archivo:
    lector = csv.DictReader(archivo, delimiter='|')
    for fila in lector:
        usuario = session.query(Usuario).filter_by(usuario=fila['Usuario']).first()
        publicacion = session.query(Publicacion).filter_by(publicacion=fila['comentario']).first()
        if usuario and publicacion:
            reaccion = Reaccion(
                usuario_id=usuario.id,
                publicacion_id=publicacion.id,
                emocion=fila['tipo emocion']
            )
            session.add(reaccion)

session.commit()  # Confirmar todas las reacciones
