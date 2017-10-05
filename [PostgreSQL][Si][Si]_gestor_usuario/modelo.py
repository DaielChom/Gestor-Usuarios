from flask_sqlalchemy import SQLAlchemy

#Inicializa base de datos
db = SQLAlchemy()

#Clase User --Las tablas son clases que heredan de Model--
class User(db.Model):

    #Nombre que tendra la base de datos
    __tablename__ = "usuarios"

    #crea parametros
    cedula = db.Column(db.String(20), primary_key = True, nullable = False)
    nombre = db.Column(db.String(20), nullable = False)
    apellido = db.Column(db.String(20), nullable = False)
    direccion = db.Column(db.String(20), nullable = False)
    correo = db.Column(db.String(40), nullable = False)
    fecha_nacimiento = db.Column(db.Date(), nullable = False)

    #Constructor
    def __init__(self, cedula, nombre, apellido, direccion, correo, fecha_nacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
