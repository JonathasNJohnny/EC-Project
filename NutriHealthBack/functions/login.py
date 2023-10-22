from schemes.schemes import *

#Obter IDs de Usuários - Start
receptionistID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Recepcionista').get().tipo_usuario_id
doctorID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Medico').get().tipo_usuario_id
administratorID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Administrador').get().tipo_usuario_id
patientID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Paciente').get().tipo_usuario_id
#Obter IDs de Usuários - End

#Funções de retorno de cada usuário - Start
def receptionistUser():
    return "Recepcionista!"
def doctorUser():
    return "Médico!"
def administratorUser():
    return "Administrador!"
def patientUser():
    return "Paciente!"
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
        if user.tipo_usuario_id.tipo_usuario_id == receptionistID:
            return "Seja bem vindo ao seu perfil de " + receptionistUser()
        elif user.tipo_usuario_id.tipo_usuario_id == doctorID:
            return "Seja bem vindo ao seu perfil de " + doctorUser()
        elif user.tipo_usuario_id.tipo_usuario_id == administratorID:
            return "Seja bem vindo ao seu perfil de " + administratorUser()
        elif user.tipo_usuario_id.tipo_usuario_id == patientID:
            return "Seja bem vindo ao seu perfil de " + patientUser()
    else:
        return "Nome de usuário ou senha estão incorretos"
#Função para utilizar no login do front, receber o usuário e mostrar - End