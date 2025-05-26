from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from genera_tablas import *
from configuracion import cadena_base_datos
 
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


# Consultar usuarios que han reaccionado a publicaciones de otro usuario específico

# Definir el nombre del usuario cuyas publicaciones queremos analizar
usuario_especifico = "Steven"

# Con el join conectamos la tabla Usuario con Reaccion, para encontrar quién reaccionó.
# Con el otro join se asocia la tabla Publicacion para filtrar por publicaciones de un usuario específico.
# Filtra las publicaciones que pertenecen a usuario_especifico. Publicacion.autor.has(usuario=usuario_especifico)
# .distinct() Garantiza que no haya nombres repetidos en los resultados.
usuarios_reaccionaron = session.query(Usuario.usuario).join(Reaccion).join(Publicacion).filter(
    Publicacion.autor.has(usuario=usuario_especifico) # .has() se usa en consultas ORM para aplicar filtros en relaciones uno a muchos o muchos a uno, verifica si existe una relación entre dos tablas.
).distinct().all()

# Mostrar resultados
print(f"Usuarios que han reaccionado a las publicaciones de {usuario_especifico}:")
for usuario in usuarios_reaccionaron:
    print(usuario.usuario)



