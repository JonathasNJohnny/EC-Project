from schemes import *
import json

def getAllQuery():
    queryBD = Consultas.select()
    queryList = [{
        'queryID': query.consultas_id,
            'medicoID': query.medico_id,
            'pacienteID': query.paciente_id,
            'data': query.data,
            'horario': query.horario,
            'dados': query.dados
        } for query in queryBD]
    return queryList

'''
from schemes import *
import json

def getAllQuery():
    queryBD = Consultas.select()
    queryList = [{
        'queryID': query.consultas_ID,
            'medicoID': query.medico_ID,
            'pacienteID': query.paciente_ID,
            'data': query.data,
            'horario': query.horario,
            'medico': {
                'userID': query.medico_ID.user_id,
                'username': query.medico_ID.user_name,
                'city': query.medico_ID.endereco_id.cidade,
                'state': query.medico_ID.endereco_id.uf,
                'neighborhood': query.medico_ID.endereco_id.bairro,
                'street': query.medico_ID.endereco_id.rua,
                'number': query.medico_ID.user_numero,
                'userType': query.medico_ID.tipo_usuario_id.tipo_usuario_nome
            },
            'paciente': {
                'userID': query.paciente_ID.user_id,
                'username': query.paciente_ID.user_name,
                'city': query.paciente_ID.endereco_id.cidade,
                'state': query.paciente_ID.endereco_id.uf,
                'neighborhood': query.paciente_ID.endereco_id.bairro,
                'street': query.paciente_ID.endereco_id.rua,
                'number': query.paciente_ID.user_numero,
                'userType': query.paciente_ID.tipo_usuario_id.tipo_usuario_nome
            }
        } for query in queryBD]
    return queryList
'''
