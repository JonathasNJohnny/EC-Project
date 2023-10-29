from schemes.schemes import*

#Criação de usuário
def createUser(username, password, cpf, typeUser):
    try:
        # Verificar se o nome de usuário já existe
        existing_user = Usuarios.get_or_none(Usuarios.user_name == username)
        if existing_user:
            print("O nome de usuário já existe e está sendo usado por outro usuário. Tente novamente com outro nome.")
            return None

        # Criar um novo usuário
        a=Usuarios.insert(user_name=username, user_senha=password, cpf=cpf, tipo_usuario_id=TiposUsuarios.get(TiposUsuarios.tipo_usuario_nome == typeUser).tipo_usuario_id)
        a.execute()

    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None
