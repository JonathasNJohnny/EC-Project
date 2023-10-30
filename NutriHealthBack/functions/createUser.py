from schemes.schemes import*

#Criação de usuário
def createUser(username, email, number, cpf, typeUser, addressCity, addressUF, addressNeighborhood, addressStreet):
    try:
        #Verificar se o nome de usuário já existe
        existing_user = Usuarios.get_or_none(Usuarios.user_name == username)
        if existing_user:
            return "2"

        #Criar Endereco
        newEndereco=Enderecos.create(cidade = addressCity, uf = addressUF, bairro = addressNeighborhood, rua = addressStreet)

        #Criar um novo usuário
        newUser = Usuarios.create(user_name=username, user_senha="12345678", user_email=email, user_numero=number, cpf=cpf, tipo_usuario_id=TiposUsuarios.get(TiposUsuarios.tipo_usuario_nome == typeUser).tipo_usuario_id, endereco_id=newEndereco)
        return "1"
    except Exception as e:
        return "3"
