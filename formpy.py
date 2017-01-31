#Librerias a usar
from wtforms import Form
from wtforms import StringField
from wtforms import DateField
from wtforms import validators
from wtforms.fields.html5 import EmailField

#Los formularios se manejan como clases
class Usuarios(Form):

    #Tipos de validaciones
    validacion_tamano = validators.length(min = 4, max = 25)
    validacion_correo = validators.Email()
    validacion_requerido = validators.Required(message="Requerido")

    #Cada input del formulario es un atributo de la clase
    #Estructura: input_name = type_name(label, validations) 
    cedula = StringField('Cedula',[validacion_tamano, validacion_requerido])
    nombres = StringField('Nombres', [validacion_tamano, validacion_requerido])
    apellidos = StringField('Apellidos', [validacion_tamano, validacion_requerido])
    direccion = StringField('Direccion', [validacion_tamano, validacion_requerido])
    correo = EmailField('Correo', [validacion_correo, validacion_requerido])
    fecha_de_nacimiento = DateField('Fecha de Nacimiento',[validacion_requerido] ,format='%d/%m/%Y')
