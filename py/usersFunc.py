from schemes import *

username = "admin"
password = "admin"

def receptionistUser():
    print("Seja bem vindo ao seu perfil de Recepcionista!")

def doctorUser():
    print("Seja bem vindo ao seu perfil de Médico!")

def administratorUser():
    print("Seja bem vindo ao seu perfil de Administrador!")

def patientUser():
    print("Seja bem vindo ao seu perfil de Paciente!")

def login(username, password):
    try:
        usuario = Usuarios.get((Usuarios.user_name == username) & (Usuarios.user_senha == password))
        return usuario
    except Usuarios.DoesNotExist:
        return None
user = login(username, password)
if user:
    if user.tipo_usuario_id.tipo_usuario_id == TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Recepcionista').get().tipo_usuario_id:
        receptionistUser()
    elif user.tipo_usuario_id.tipo_usuario_id == TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Medico').get().tipo_usuario_id:
        doctorUser()
    elif user.tipo_usuario_id.tipo_usuario_id == TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Administrador').get().tipo_usuario_id:
        administratorUser()
    elif user.tipo_usuario_id.tipo_usuario_id == TiposUsuarios.select().where(TiposUsuarios.tipo_usuario_nome == 'Paciente').get().tipo_usuario_id:
        patientUser()
else:
    print("Nome de usuário ou senha estão incorretos")