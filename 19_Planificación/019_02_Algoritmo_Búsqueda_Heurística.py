#Algoritmo de Búsqueda Heurística para Planificación

from queue import PriorityQueue

def a_estrella(estado_inicial, es_objetivo, acciones_aplicables, heuristica):
    frontera = PriorityQueue()
    frontera.put((0, estado_inicial, []))
    explorados = set()

    while not frontera.empty():
        costo, estado, camino = frontera.get()

        if es_objetivo(estado):
            return camino

        explorados.add(estado)

        for accion, estado_siguiente in acciones_aplicables(estado):
            if estado_siguiente not in explorados:
                costo_total = costo + heuristica(estado_siguiente)
                frontera.put((costo_total, estado_siguiente, camino + [accion]))

    return None

# Ejemplo de uso
def es_objetivo(estado):
    return estado == 5

def acciones_aplicables(estado):
    return [('Avanzar', estado + 1), ('Retroceder', estado - 1)]

def heuristica(estado):
    return abs(estado - 5)

estado_inicial = 1
solucion = a_estrella(estado_inicial, es_objetivo, acciones_aplicables, heuristica)
print("Solución:", solucion)
