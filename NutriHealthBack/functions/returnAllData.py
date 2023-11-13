from schemes.schemes import *
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
