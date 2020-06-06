from flask import Flask
from flask import jsonify  #jsonify libreria q convierte de Object Json a un formato bonito muy parecido a dumps
from flask import request   # libreria para poder obtener la peticion
import json   # loads libreria q convierte String a Object json(diccionario), dumps lo contrario  

app = Flask(__name__)

users = [
    {
        "Username": "Admin",
        "Password": "555"
    },
    {
        "Username": "Mile",
        "Password": "888"
    }
]
#lectura de usuarios
@app.route('/users', methods=["GET"])       #Peticion Get a la ruta /users retorna todos los usuarios
def getAllUsers():
    return jsonify(users), 200


@app.route('/users/<string:username>', methods=["GET"])       #Peticion Get retorna el usuario especificado
def getUserByUsername(username):
    result = next(user for user in users if user["Username"] == username)
    if result is not None:
        return jsonify(result), 200
    else:
        return "User not found", 404


#crear usuarios
@app.route('/users', methods=["POST"])       #Peticion post que crea un usuario
def addUser():
    body = json.loads(request.data)
    print(body)
    user = body["Username"]
    passw = body["Password"]

    newUser = {
        "Username": user,
        "Password": passw
    }

    users.append(newUser)
    l = jsonify(newUser)
    print(l)
    return l, 200

if __name__ == "__main__":
    app.run(debug=True)