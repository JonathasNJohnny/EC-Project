from flask import Flask, request, jsonify
from functions.login import login
from functions.returnUsers import getAllUsers

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

if __name__ == "__main__":
    app.run(debug=True)
