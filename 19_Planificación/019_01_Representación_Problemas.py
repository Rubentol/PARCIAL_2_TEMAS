#Representación de Problemas de Planificación

from pyddl import Domain, Problem, Action, neg, Planner

# Definir el dominio en PDDL
domain = Domain((
    Action(
        'mover',
        parameters=(('ubicacion', 'origen'), ('ubicacion', 'destino')),
        preconditions=(('en', 'robot', 'origen'),),
        effects=(('en', 'robot', 'destino'), ('no_en', 'robot', 'origen'))
    ),
))

# Definir el problema en PDDL
problem = Problem(
    domain,
    {
        'ubicacion': ('A', 'B', 'C'),
        'robot': ('R',)
    },
    init=(('en', 'robot', 'A'),),
    goal=(('en', 'robot', 'C'),)
)

# Resolver el problema usando un planificador (PyDDL)
planificador = Planner(domain, problem)
solucion = planificador.plan()

print("Plan de acción:")
for accion in solucion:
    print(accion)
