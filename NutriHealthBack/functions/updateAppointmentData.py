from schemes.schemes import *

def updateAppointmentData(appointmentID, newData=None):
    try:
        consulta = Consultas.get(onsultas_id=appointmentID)
        consulta.dados = newData
        consulta.save
    except DoesNotExist:
        return "2"