#Evaluación de Fórmulas Lógicas

def evaluar_formula_logica(formula, asignacion):
    """
    Evalúa una fórmula lógica dada una asignación de variables.
    Args:
        formula (str): Fórmula lógica en notación infix (por ejemplo, "A AND B OR NOT C").
        asignacion (dict): Asignación de variables (por ejemplo, {"A": True, "B": False, "C": True}).
    Returns:
        bool: Resultado de evaluar la fórmula con la asignación dada.
    """
    # Reemplazar las variables en la fórmula con sus valores de asignación
    for variable, valor in asignacion.items():
        formula = formula.replace(variable, str(valor))
    # Evaluar la fórmula usando la función eval() de Python
    resultado = eval(formula)
    return resultado

# Ejemplo de uso
formula = "(A AND B) OR (NOT C)"
asignacion = {"A": True, "B": False, "C": True}
resultado = evaluar_formula_logica(formula, asignacion)
print("Resultado de la fórmula:", resultado)
