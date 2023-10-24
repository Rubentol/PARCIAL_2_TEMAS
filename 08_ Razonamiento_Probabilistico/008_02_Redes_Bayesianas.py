#Redes Bayesianas

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Definir estructura de la red bayesiana
modelo = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Definir las probabilidades condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.7], [0.3]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.8], [0.2]])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.9, 0.6, 0.8, 0.1], [0.1, 0.4, 0.2, 0.9]],
                  evidence=['A', 'B'], evidence_card=[2, 2])

# Asignar las probabilidades condicionales al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificar la validez del modelo
print("El modelo es válido?", modelo.check_model())
