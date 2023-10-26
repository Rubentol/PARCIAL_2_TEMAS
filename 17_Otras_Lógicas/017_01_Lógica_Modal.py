#Lógica Modal

from sympy import symbols
from sympy.logic.modal import Valid

# Definir símbolos como variables
p, q = symbols('p q')

# Definir una fórmula modal
formula_modal = Valid(p >> q)

# Verificar si la fórmula es válida en el marco K
es_valida = formula_modal.evaluate()
print("La fórmula modal es válida." if es_valida else "La fórmula modal no es válida.")
