from schemes.schemes import *

def createAppointment(medico_id, paciente_id, data, horario, dados=None):
    try:
        nova_consulta = Consultas.create(medico_id=medico_id, paciente_id=paciente_id, data=data, horario=horario, dados=dados)
        return "1"
    except Exception as e:
        print(f"Erro ao criar consulta: {e}")
        return "2"