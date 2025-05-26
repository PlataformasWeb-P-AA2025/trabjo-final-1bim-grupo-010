from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import func # Permite acceder a las funciones de agregación y otras funciones SQL directamente dentro de SQLAlchemy.
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


# Obtener un reporte de reacciones en función del número de veces que fueron usadas.
reporte_reacciones = session.query(Reaccion.emocion, func.count(Reaccion.emocion)).group_by(Reaccion.emocion).all() # Aplica la función SQL COUNT() para contar cuántas veces aparece cada tipo de emoción.
# Agrupa los registros por el campo emocion, permitiendo contar cada tipo de reacción por separado.

# Mostrar el reporte
print("Reporte de reacciones:")
for emocion, cantidad in reporte_reacciones:
    print(f"{emocion}: {cantidad} veces")
