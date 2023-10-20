#Busqueda No Informada "Costos Uniformes"

import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append((v, peso))

    def busqueda_costos_uniformes(self, inicio, objetivo):
        cola = []
        heapq.heappush(cola, (0, inicio))  # (costo acumulado, nodo)
        visitado = set()

        while cola:
            costo, nodo_actual = heapq.heappop(cola)

            if nodo_actual in visitado:
                continue

            visitado.add(nodo_actual)

            if nodo_actual == objetivo:
                return costo

            if nodo_actual in self.grafo:
                for vecino, peso in self.grafo[nodo_actual]:
                    if vecino not in visitado:
                        heapq.heappush(cola, (costo + peso, vecino))

        return float('inf')  # Si no se encuentra un camino al objetivo

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista('A', 'B', 4)
grafo.agregar_arista('A', 'C', 2)
grafo.agregar_arista('B', 'C', 5)
grafo.agregar_arista('B', 'D', 10)
grafo.agregar_arista('C', 'D', 3)

inicio = 'A'
objetivo = 'B'

costo_camino = grafo.busqueda_costos_uniformes(inicio, objetivo)
if costo_camino != float('inf'):
    print(f"El costo del camino más corto desde {inicio} hasta {objetivo} es: {costo_camino}")
else:
    print(f"No hay camino desde {inicio} hasta {objetivo}")
