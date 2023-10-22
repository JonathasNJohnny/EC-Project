from schemes import *

receptionistID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Recepcionista').get().tipo_usuario_id
doctorID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Medico').get().tipo_usuario_id
administratorID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Administrador').get().tipo_usuario_id
patientID = TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Paciente').get().tipo_usuario_id

username = "admin"
password = "admin"

def receptionistUser():
    return "Seja bem vindo ao seu perfil de Recepcionista!"

def doctorUser():
    return "Seja bem vindo ao seu perfil de Médico!"

def administratorUser():
    return "Seja bem vindo ao seu perfil de Administrador!"

def patientUser():
    return "Seja bem vindo ao seu perfil de Paciente!"

def getUser(username, password):
    try:
        usuario = Usuarios.get((Usuarios.user_name == username) & (Usuarios.user_senha == password))
        return usuario
    except Usuarios.DoesNotExist:
        return None

def login(username, password):
    user = getUser(username, password)
    if user:
        if user.tipo_usuario_id.tipo_usuario_id == receptionistID:
            return receptionistUser()
        elif user.tipo_usuario_id.tipo_usuario_id == doctorID:
            return doctorUser()
        elif user.tipo_usuario_id.tipo_usuario_id == administratorID:
            return administratorUser()
        elif user.tipo_usuario_id.tipo_usuario_id == patientID:
            return patientUser()
    else:
        return "Nome de usuário ou senha estão incorretos"
