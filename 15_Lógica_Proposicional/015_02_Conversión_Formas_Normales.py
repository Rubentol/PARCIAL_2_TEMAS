#Conversión entre Formas Normales

from sympy import symbols, Not, Or, And, to_cnf

# Definir símbolos como variables proposicionales
A, B, C = symbols('A B C')

# Definir la fórmula en lógica proposicional
formula = Or(And(A, B), Not(C))

# Convertir la fórmula a CNF
cnf_formula = to_cnf(formula)

print("Fórmula en CNF:", cnf_formula)
