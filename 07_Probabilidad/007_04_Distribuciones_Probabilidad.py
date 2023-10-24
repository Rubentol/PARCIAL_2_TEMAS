#Distribuciones de Probabilidad

import random
from collections import Counter

# Simulación de lanzamiento de un dado y conteo de ocurrencias
num_lanzamientos = 1000
resultados = [random.randint(1, 6) for _ in range(num_lanzamientos)]
frecuencia = Counter(resultados)

# Probabilidad empírica de cada número
probabilidad_empirica = {numero: frecuencia[numero] / num_lanzamientos for numero in frecuencia}
print("Probabilidad empírica de cada número en un dado:", probabilidad_empirica)
