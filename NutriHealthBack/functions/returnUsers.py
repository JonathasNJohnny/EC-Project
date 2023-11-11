from schemes.schemes import *
import json

def getAllUsers():
    usersBD = Usuarios.select()
    userList = [{'userID': user.user_id, 'username': user.user_name, 'city': user.endereco_id.cidade, 'state': user.endereco_id.uf, 'neighborhood': user.endereco_id.bairro, 'street': user.endereco_id.rua, 'number': user.user_numero, 'userType': user.tipo_usuario_id.tipo_usuario_nome} for user in usersBD]
    return userList
