#Librerias a usar de Flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask_wtf import CsrfProtect

#Libreria para manejo de ajax
import json

#Configuraciones --Desarrollador--
from config import DevelopmentConfig

#Estructura del formulario
import formpy

#Modelo de datos
from modelo import db
from modelo import User

#Crea instacia de Flask
app = Flask(__name__)
#Aplica configuraciones --Desarrollador--
app.config.from_object(DevelopmentConfig)
#Instancia de cifrado --Para seguridad de form--
csrf = CsrfProtect()

#Ruta usuarios, permite agregar, consultar, eliminar, modificar
@app.route('/usuarios', methods = ['GET','POST'])
@app.route('/usuarios/<cedula>', methods = ['GET','PUT','DELETE'])
#Funcion usuario, lleva acabo las tareas del servidor al acceder a /usuario
def usuario(cedula = None):

    #listado de clases --auxiliar para ocultar y mostrar elementos con un boton--
    clases_css = ['hidden','ancho-form','ancho-consulta','display-block']
    #titulo de la pestaña
    title = 'Usuarios'
    #Instancia del formulario --Vacia al principio--
    usuarios_form = formpy.Usuarios(None)

    #Tareas al recibir peticion GET
    if request.method == 'GET' and cedula:
        #Consulta en la base de datos
        usuario = User.query.filter_by(cedula = cedula).first()
        #Si el usuario existe
        if usuario is not None:
            #Toma los datos de la base y los agrega a la instancia del formulario
            usuarios_form.cedula.data = usuario.cedula
            usuarios_form.nombres.data = usuario.nombre
            usuarios_form.apellidos.data = usuario.apellido
            usuarios_form.direccion.data = usuario.direccion
            usuarios_form.correo.data = usuario.correo
            usuarios_form.fecha_de_nacimiento.data = usuario.fecha_nacimiento

        #Si el usuario no existe
        else:
            #Regresa a /usuarios e indica que el usuario no existe
            switch(clases_css)
            error_message = 'error'
            flash(error_message)
            return redirect(url_for('usuario'))

        #Cambias las clases CSS para mostrar los otros input
        switch(clases_css)

    #Tareas al recibir peticion POST
    if request.method == 'POST':
        #Crea instancia del formulario que trae la peticion
        usuarios_form = formpy.Usuarios(request.form)

        #Validar campos
        if usuarios_form.validate():
            #Consulta existencia del usuario a agregar
            cedula_consulta = User.query.filter_by(cedula = usuarios_form.cedula.data).first()

            #Si no existe, lo crea.
            if cedula_consulta is None:
                #Crea una instancia del modelo con los datos del formulario
                usuario = User(usuarios_form.cedula.data,
                                usuarios_form.nombres.data,
                                usuarios_form.apellidos.data,
                                usuarios_form.direccion.data,
                                usuarios_form.correo.data,
                                usuarios_form.fecha_de_nacimiento.data)

                #agrega el usuario yactualiza la base de datos
                db.session.add(usuario)
                db.session.commit()
                #confirma al usuario
                message = 'success'
                flash(message)
                return redirect(url_for('usuario'))

            #Si ya existe informa al usuario
            else:
                message = 'exist'
                flash(message)
                return redirect(url_for('usuario'))

    #Tareas al recibir peticion PUT
    if request.method == 'PUT':
        #Toma los datos del form
        usuarios_form = formpy.Usuarios(request.form)

        #Realiza la consulta
        usuario_db = User.query.get(cedula)

        #Acutaliza los cambios al usuario consultado
        usuario_db.nombre = usuarios_form.nombres.data
        usuario_db.apellido = usuarios_form.apellidos.data
        usuario_db.direccion = usuarios_form.direccion.data
        usuario_db.correo = usuarios_form.correo.data
        usuario_db.fecha_nacimiento = usuarios_form.fecha_de_nacimiento.data
        #actualiza la base de datos
        db.session.commit()
        return json.dumps({'status':200})

    #Tareas al recibir peticion DELETE
    if request.method == 'DELETE':
        db.session.delete(User.query.get(cedula))
        db.session.commit()
        return json.dumps({'status':200})

    return render_template('usuarios.html', title = title, clases = clases_css, formulario = usuarios_form)

#Funcion para ocular y mostrar los input
def switch(clases_css):
    clases_css.reverse()


if __name__ == '__main__':
    #Inicia el cifrado y la base datos en la instancia de Flask
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        #Crea las tablas que hacen falta
        db.create_all()
    app.run(port = 8000)
