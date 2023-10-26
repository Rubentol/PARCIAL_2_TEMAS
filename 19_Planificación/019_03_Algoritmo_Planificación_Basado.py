#Algoritmo de Planificación Basado en Reglas

class ReglaProduccion:
    def __init__(self, condicion, accion):
        self.condicion = condicion
        self.accion = accion

def planificacion_basada_en_reglas(estado_inicial, reglas):
    estado_actual = estado_inicial
    plan = []

    while True:
        accion_encontrada = False

        for regla in reglas:
            if regla.condicion(estado_actual):
                plan.append(regla.accion)
                estado_actual = regla.accion(estado_actual)
                accion_encontrada = True
                break

        if not accion_encontrada:
            break

    return plan

# Ejemplo de uso
def condicion(estado):
    return estado < 5

def accion(estado):
    return estado + 1

reglas = [ReglaProduccion(condicion, accion)]
estado_inicial = 1

plan = planificacion_basada_en_reglas(estado_inicial, reglas)
print("Plan de acción:", plan)
