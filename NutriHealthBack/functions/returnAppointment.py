from schemes.schemes import *
import json

def getAllAppointments():
    appointmentDB = Consultas.select()
    appointmentList = [{
        'consultaID': appointment.consultas_id,
            'medicoID': appointment.medico_id.user_id,
            'pacienteID': appointment.paciente_id.user_id,
            'data': appointment.data,
            'horario': appointment.horario,
            'dados': appointment.dados
        } for appointment in appointmentDB]
    return appointmentList