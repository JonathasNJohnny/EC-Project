from schemes.schemes import *

def createAppointment(medicID, patientID, date, time, reason=None):
    try:
        nova_consulta = Consultas.create(medico_id=medicID, paciente_id=patientID, data=date, horario=time, motivo=reason)
        return "1"
    except Exception as e:
        print(f"Erro ao criar consulta: {e}")
        return "2"