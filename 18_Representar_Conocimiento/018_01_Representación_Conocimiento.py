#Representación del Conocimiento en Grafos

class GrafoConocimiento:
    def __init__(self):
        self.grafo = {}

    def agregar_relacion(self, entidad1, entidad2):
        if entidad1 in self.grafo:
            self.grafo[entidad1].append(entidad2)
        else:
            self.grafo[entidad1] = [entidad2]

    def obtener_relaciones(self, entidad):
        if entidad in self.grafo:
            return self.grafo[entidad]
        else:
            return []

# Ejemplo de uso
grafo_conocimiento = GrafoConocimiento()
grafo_conocimiento.agregar_relacion("perro", "animal")
grafo_conocimiento.agregar_relacion("gato", "animal")
grafo_conocimiento.agregar_relacion("pájaro", "animal")

entidad = "perro"
relaciones = grafo_conocimiento.obtener_relaciones(entidad)
print(f"Relaciones de {entidad}: {relaciones}")
