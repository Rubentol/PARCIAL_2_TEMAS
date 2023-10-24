#Filtro de Partículas

import numpy as np
from numpy.random import uniform

# Inicialización de partículas
num_particulas = 1000
particulas = uniform(low=0, high=1, size=num_particulas)

# Actualización de partículas basada en medidas
medicion = 0.6
ruido_medicion = 0.2
pesos = np.exp(-0.5 * ((particulas - medicion) / ruido_medicion) ** 2)
pesos /= sum(pesos)

# Muestreo basado en pesos
indices_muestreados = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos)
particulas_muestreadas = particulas[indices_muestreados]

print("Partículas Muestreadas:", particulas_muestreadas)
