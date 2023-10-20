#Busqueda No Informada "Profundidad"

from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)

    def dfs_util(self, nodo, visitado):
        visitado[nodo] = True
        print(nodo, end=" ")

        for i in self.grafo[nodo]:
            if not visitado[i]:
                self.dfs_util(i, visitado)

    def busqueda_profundidad(self, inicio):
        visitado = [False] * (max(self.grafo) + 1)
        self.dfs_util(inicio, visitado)

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido en profundidad (DFS) empezando desde el nodo 2:")
grafo.busqueda_profundidad(2)
