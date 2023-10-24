#Algoritmos de Consistencia

def forward_checking(csp):
    return fc({}, csp)

def fc(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment
    
    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            # Realizar la propagación de restricciones
            inferences = inference(var, value, assignment, csp)
            if inferences is not None:
                assignment.update(inferences)
                result = fc(assignment, csp)
                if result:
                    return result
            del assignment[var]
            # Deshacer las inferences
            undo_inferences(inferences, assignment, csp)
    return None

def inference(var, value, assignment, csp):
    # Realizar la propagación de restricciones y devolver las inferencias
    pass

def undo_inferences(inferences, assignment, csp):
    # Deshacer las inferencias realizadas
    pass
