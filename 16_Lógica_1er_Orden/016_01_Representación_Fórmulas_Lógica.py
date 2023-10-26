#Representación de Fórmulas en Lógica de Primer Orden

from sympy import symbols, Forall, Implies

# Definir símbolos como variables
x, y = symbols('x y')

# Crear una fórmula en lógica de primer orden
formula = Forall(x, Implies(x > 0, y > 0))

print("Fórmula en lógica de primer orden:", formula)
