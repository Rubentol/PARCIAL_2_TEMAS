#Modelos Gráficos Probabilísticos

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
import numpy as np

# Definir la estructura de la red bayesiana
model = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Definir las distribuciones condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                  values=[[0.9, 0.8, 0.7, 0.1], [0.1, 0.2, 0.3, 0.9]],
                  evidence=['A', 'B'], evidence_card=[2, 2])

# Asociar las distribuciones condicionales con la red
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificar la validez de la red bayesiana
assert model.check_model()

# Calcular la probabilidad conjunta P(A=1, B=0, C=1)
result = np.prod(model.predict_proba([[1, 0, 1]])[0].values)
print("Probabilidad conjunta P(A=1, B=0, C=1): {:.2f}".format(result))