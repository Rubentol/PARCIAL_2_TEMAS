#Representación del Conocimiento en Ontologías

from owlready2 import *

# Crear una ontología
onto = Ontology("http://www.ejemplo.com/ontologia.owl")

# Definir clases en la ontología
class Animal(Thing):
    namespace = onto

class Mamifero(Animal):
    namespace = onto

class Ave(Animal):
    namespace = onto

# Asignar individuos a las clases
perro = Animal("perro")
gato = Animal("gato")
pajaro = Ave("pajaro")

# Guardar la ontología en un archivo OWL
onto.save(file = "ontologia.owl", format = "rdfxml")
