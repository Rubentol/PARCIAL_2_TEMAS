#Inferencia en Lógica de Primer Orden

from sympy import And

# Definir símbolos como variables
A, B, C = symbols('A B C')

# Definir premisas en lógica de primer orden
premisas = [Implies(A, B), And(A, C)]

# Inferir una conclusión usando lógica de primer orden
conclusion = Implies(C, B)

# Verificar si la conclusión sigue de las premisas usando inferencia
es_valido = conclusion in solve(premisas)

print("La conclusión es válida." if es_valido else "La conclusión no es válida.")
