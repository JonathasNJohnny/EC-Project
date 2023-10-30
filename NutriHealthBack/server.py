from flask import Flask, request, jsonify
from functions.login import login
from functions.returnUsers import getAllUsers
from functions.createUser import createUser

app = Flask(__name__)

#Rota para efetuar o login
@app.route("/api/login", methods=['GET'])
def login_route():
    name = request.args.get('name')
    password = request.args.get('password')
    result = login(name, password)
    return jsonify({"message": result})

#Rota para obter todos os usuários
@app.route("/api/getUsers", methods=['GET'])
def get_users_route():
    result = getAllUsers()
    return jsonify(result)

#Rota para cadastrar usuários
@app.route("/api/registerUser", methods=['GET'])
def register_user_route():
    name = request.args.get('name')
    email = request.args.get('email')
    number = request.args.get('number')
    cpf = request.args.get('cpf')
    typeUser = request.args.get('typeUser')
    addressCity = request.args.get('addressCity')
    addressUF = request.args.get('addressUF')
    addressNeighborhood = request.args.get('addressNeighborhood')
    addressStreet = request.args.get('addressStreet')
    return createUser(name, email, number, cpf, typeUser, addressCity, addressUF, addressNeighborhood, addressStreet)

if __name__ == "__main__":
    app.run(debug=True)
