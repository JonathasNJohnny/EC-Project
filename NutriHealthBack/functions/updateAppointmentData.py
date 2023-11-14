from schemes.schemes import *

def updateAppointmentData(appointmentID, newData=None):
    try:
        consulta = Consultas.get(consultas_id=appointmentID)
        consulta.dados = newData
        consulta.save()
        return "1"
    except DoesNotExist:
        return "2"