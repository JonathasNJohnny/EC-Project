from peewee import *

db = PostgresqlDatabase('clinic', user='postgres', password='12345678', host='localhost', port=5432)
class TiposUsuarios(Model):
    tipo_usuario_id = IntegerField(primary_key=True)
    tipo_usuario_nome = CharField(max_length=50, null=False)

    class Meta:
        database = db
        table_name = 'tipos_usuarios'

class Usuarios(Model):
    user_id = IntegerField(primary_key=True)
    user_name = CharField(max_length=50, null=False)
    user_senha = CharField(max_length=50, null=False)
    cpf = CharField(max_length=50, null=False)
    tipo_usuario_id = ForeignKeyField(TiposUsuarios, field='tipo_usuario_id', backref='usuarios')

    class Meta:
        database = db

db.connect()
db.close()