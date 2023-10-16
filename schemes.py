from peewee import *

db = PostgresqlDatabase('clinic', user='postgres', password='12345678', host='localhost', port=5432)

class TiposUsuarios(Model):
    tipo_Usuario_ID = IntegerField(primary_key=True)
    tipo_Usuario_Nome = CharField(max_length=50, null=False)

    class Meta:
        database = db

class Usuarios(Model):
    user_ID = IntegerField(primary_key=True)
    user_Name = CharField(max_length=50, null=False)
    user_Senha = CharField(max_length=50, null=False)
    tipo_Usuario_ID = ForeignKeyField(TiposUsuarios, backref='usuarios')

    class Meta:
        database = db
def dropAndCreate():
    db.drop_tables([TiposUsuarios, Usuarios], safe=True, cascade=True)
    db.create_tables([TiposUsuarios, Usuarios])

db.connect()
dropAndCreate()
db.close()