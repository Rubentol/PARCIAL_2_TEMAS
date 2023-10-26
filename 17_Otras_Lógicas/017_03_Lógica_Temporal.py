#Lógica Temporal

from temporal_logic.formulas import TemporalLogicParser
from temporal_logic.model import TemporalState

# Definir una fórmula temporal
formula_temporal = "G(p -> XF(q))"

# Crear un objeto de análisis para la fórmula temporal
parser = TemporalLogicParser()
formula = parser.parse(formula_temporal)

# Definir un estado temporal
estado_temporal = TemporalState({"p": True, "q": False})

# Evaluar la fórmula temporal en el estado dado
resultado = formula.evaluate(estado_temporal)

print("El resultado de la fórmula temporal es:", resultado)
