from schemes.schemes import *
import json

#Obter IDs de Usuários - Start
receptionist = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Recepcionista').get()
receptionist = [receptionist.tipo_usuario_id, receptionist.tipo_usuario_nome]
doctor = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Medico').get()
doctor = [doctor.tipo_usuario_id, doctor.tipo_usuario_nome]
administrator = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Administrador').get()
administrator = [administrator.tipo_usuario_id, administrator.tipo_usuario_nome]
patient = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Paciente').get()
patient = [patient.tipo_usuario_id, patient.tipo_usuario_nome]
#Obter IDs de Usuários - End

#Função para retornar um Json do usuário - Start
def getJson(user_id, user_type):
    return json.dumps({"user_id": user_id, "user_type": user_type})
#Função para retornar um Json do usuário - End

#Funções de retorno de cada usuário - Start
def receptionistUser():
    return getJson(receptionist[0], receptionist[1])
def doctorUser():
    return getJson(doctor[0], doctor[1])
def administratorUser():
    return getJson(administrator[0], administrator[1])
def patientUser():
    return getJson(patient[0], patient[1])
#Funções de retorno de cada usuário - End

#Função para retornar o usuário - Start
def getUser(username, password):
    try:
        usuario = Usuarios.get((Usuarios.user_name == username) & (Usuarios.user_senha == password))
        return usuario
    except Usuarios.DoesNotExist:
        return None
#Função para retornar o usuário - End

#Função para utilizar no login do front, receber o usuário e mostrar - Start
def login(username, password):
    user = getUser(username, password)
    if user:
        if user.tipo_usuario_id.tipo_usuario_id == receptionist[0]:
            return receptionistUser()
        elif user.tipo_usuario_id.tipo_usuario_id == doctor[0]:
            return doctorUser()
        elif user.tipo_usuario_id.tipo_usuario_id == administrator[0]:
            return administratorUser()
        elif user.tipo_usuario_id.tipo_usuario_id == patient[0]:
            return patientUser()
    else:
        return "Nome de usuário ou senha estão incorretos"
#Função para utilizar no login do front, receber o usuário e mostrar - End