# Inferencia Bayesiana

from pgmpy.inference import VariableElimination

# Crear un objeto de inferencia usando Variable Elimination
inferencia = VariableElimination(modelo)

# Calcular la probabilidad P(C=1) usando inferencia bayesiana
resultado = inferencia.query(variables=['C'])
print("Probabilidad P(C=1):", resultado.values[1])

