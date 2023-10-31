from flask import Flask, request, jsonify
from functions.login import login
from functions.returnUsers import getAllUsers
from functions.createUser import createUser
from functions.createAppointment import createAppointment

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

#Rota para criar um usuário
@app.route("/api/createUser", methods=['POST'])
def create_user_route():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        number = data.get('number')
        cpf = data.get('cpf')
        typeUser = data.get('typeUser')
        addressCity = data.get('addressCity')
        addressUF = data.get('addressUF')
        addressNeighborhood = data.get('addressNeighborhood')
        addressStreet = data.get('addressStreet')
        result = createUser(username, email, number, cpf, typeUser, addressCity, addressUF, addressNeighborhood, addressStreet)
        return result

#Rota para criar uma consulta
@app.route("/api/createAppointment", methods=['POST'])
def create_appointment_route():
    medico_id = int(request.form.get('medico_id'))
    paciente_id = int(request.form.get('paciente_id'))
    data = request.form.get('data')
    horario = request.form.get('horario')
    dados = request.form.get('dados')
    return createAppointment(medico_id, paciente_id, data, horario, dados)

if __name__ == "__main__":
    app.run(debug=True)