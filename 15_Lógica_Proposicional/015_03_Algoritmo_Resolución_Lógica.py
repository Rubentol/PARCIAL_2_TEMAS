#Algoritmo de Resolución para Lógica Proposicional

from sympy import symbols, Not, Or, ask, Q

# Definir símbolos como variables proposicionales
A, B, C = symbols('A B C')

# Definir las premisas y la conclusión
premisas = [Or(A, B), Or(Not(A), C), Or(Not(B), C)]
conclusion = C

# Aplicar resolución para verificar si la conclusión es válida dadas las premisas
es_valido = ask(Q.all(Or(*premisa, Not(conclusion)) for premisa in premisas), Q.resolution)

print("La conclusión es válida." if es_valido else "La conclusión no es válida.")
