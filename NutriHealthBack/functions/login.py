from schemes.schemes import *
import json

# Obtém os tipos de usuário e armazena em um dicionário
userTypes = {}
for tipoUsuario in TiposUsuarios.select():
    userTypes[tipoUsuario.tipo_usuario_id] = tipoUsuario.tipo_usuario_nome

# Função para retornar um JSON do usuário
def getJson(userID, userTypeID):
    userName = userTypes.get(userTypeID)
    return json.dumps({"user_id": userID, "user_type": userName})

# Função para retornar o usuário
def getUser(username, password):
    try:
        user = Usuarios.get((Usuarios.user_name == username) & (Usuarios.user_senha == password))
        return user
    except Usuarios.DoesNotExist:
        return None

# Função para utilizar no login do front, receber o usuário e mostrar
def login(username, password):
    user = getUser(username, password)
    if user:
        return getJson(user.user_id, user.tipo_usuario_id.tipo_usuario_id)
    else:
        return None
