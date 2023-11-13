from schemes.schemes import *

def getAllAppointments():
    appointmentDB = Consultas.select()
    appointmentList = [{
        'appointmentID': appointment.consultas_id,
            'medicID': appointment.medico_id.user_id,
            'patientID': appointment.paciente_id.user_id,
            'patientName':appointment.paciente_id.user_name,
            'date': appointment.data,
            'time': appointment.horario,
            'reason': appointment.motivo,
            'data': appointment.dados
        } for appointment in appointmentDB]
    return appointmentList