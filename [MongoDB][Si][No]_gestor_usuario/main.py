from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongo = MongoClient('localhost',27017)
db = mongo.usuario_test

@app.route('/usuario', methods=['GET','POST'])
@app.route('/usuario/<nombre>', methods=['GET', 'PUT', 'DELETE'])
def usuario(nombre = None):

    if request.method == 'GET':
        if nombre is not None:
            print(nombre)
            usuario = db.usuario.find_one({'nombre':nombre})
            if usuario:
                return jsonify({'nombre':usuario['nombre'], 'edad':usuario['edad']})
            else:
                return "Usuario no existe"
        else:
            return "Bienvenido"

    if request.method == 'POST':
        usuario_nombre = request.json['nombre']
        usuario_edad = request.json['edad']
        db.usuario.insert_one({'nombre':usuario_nombre, 'edad':usuario_edad})
        return "OK"

    if request.method == 'PUT':
        usuario = db.usuario.find_one({'nombre':nombre})
        if usuario:
            db.usuario.update_one({'nombre':nombre},{'$set':{'edad':request.json['edad']}})
            return "OK"
        else:
            return "Usuario no existe"

    if request.method == 'DELETE':
        usuario = db.usuario.find_one({'nombre':nombre})
        if usuario:
            db.usuario.delete_one({'nombre':nombre})
            return "OK"
        else:
            return "Usuario no existe"


if __name__ == '__main__':
    app.run(debug=True)
