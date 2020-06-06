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
    user = body["Username"]
    passw = body["Password"]

    newUser = {
        "Username": user,
        "Password": passw
    }

    users.append(newUser)
    return jsonify(newUser), 200

# borrar usuarios
@app.route('/users/<string:username>', methods=['DELETE'])
def deleteUser(username):
    userFound = None
    for index, user in enumerate(users):
        print(index)
        if user['Username'] == username:
            userFound = user
            users.pop(index)
    
    if userFound is not None:
        return 'User Deleted', 200
    else:
        return 'User not found', 404

#actualizar un usuario

@app.route('/users/<string:username>', methods=['PUT'])
def updateUser(username):
    userUpdate = None
    for index, user in enumerate(users):
        if user['Username'] == username:
            userUpdate = user
            body = json.loads(request.data)
            newUser = body["Username"]
            newPassw = body["Password"]

            updatedUser = {
            "Username": newUser,
            "Password": newPassw
            }
            users[index] = updatedUser
    
    if userUpdate is not None:
        return 'User Updated', 200
    else:
        return 'User not Found', 404
        
if __name__ == "__main__":
    app.run(debug=True)