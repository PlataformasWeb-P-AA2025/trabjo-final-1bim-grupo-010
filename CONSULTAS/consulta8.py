from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
