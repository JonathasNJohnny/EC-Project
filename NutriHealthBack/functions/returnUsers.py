from schemes.schemes import *
import json

def getAllUsers():
    usersBD = Usuarios.select()
    userList = [{'userID': user.user_id, 'username': user.user_name, 'userPassword': user.user_senha, 'typeUserID': user.tipo_usuario_id.tipo_usuario_id} for user in usersBD]
    return userList