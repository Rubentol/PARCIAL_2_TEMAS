#Filtro de Kalman

import numpy as np

# Inicialización de variables
estimacion_previa = 0
error_previo = 1

# Mediciones y ruido del proceso
medicion = 3
ruido_medicion = 2

# Predicción del siguiente estado
ganancia_kalman = error_previo / (error_previo + ruido_medicion)
estimacion_posterior = estimacion_previa + ganancia_kalman * (medicion - estimacion_previa)

# Actualización del error de estimación
error_posterior = (1 - ganancia_kalman) * error_previo

print("Estimación Posterior:", estimacion_posterior)
print("Error Posterior:", error_posterior)
