from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


#Listar publicaciones de un usuario.

usuarios = session.query(Usuario).filter(Usuario.nombre.like("%Shelley%")).all()
print(usuarios)