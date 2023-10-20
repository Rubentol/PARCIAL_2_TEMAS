#Busqueda No Informada "Amplitud"

from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)

    def busqueda_amplitud(self, inicio):
        visitado = [False] * (max(self.grafo) + 1)
        cola = []
        resultado = []

        cola.append(inicio)
        visitado[inicio] = True

        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo)

            for i in self.grafo[nodo]:
                if not visitado[i]:
                    cola.append(i)
                    visitado[i] = True

        return resultado

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido en amplitud (BFS) empezando desde el nodo 2:")
print(grafo.busqueda_amplitud(2))
