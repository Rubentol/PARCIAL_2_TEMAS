#Backtracking

def backtracking(csp):
    return backtrack({}, csp)

def backtrack(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment  # Si todas las variables están asignadas, hemos encontrado una solución
    
    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            result = backtrack(assignment, csp)
            if result:
                return result
            del assignment[var]  # Deshacer la asignación si no lleva a una solución
    return None  # No hay solución para el CSP

def select_unassigned_variable(csp, assignment):
    # Seleccionar una variable no asignada
    pass

def order_domain_values(var, assignment, csp):
    # Ordenar los valores de dominio de la variable
    pass

def is_consistent(var, value, assignment, csp):
    # Verificar si la asignación es consistente con las restricciones
    pass
