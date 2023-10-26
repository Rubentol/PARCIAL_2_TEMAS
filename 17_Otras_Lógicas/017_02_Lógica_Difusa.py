#Lógica Difusa

import numpy as np
import skfuzzy as fuzz

# Definir el universo y las funciones de pertenencia
x = np.arange(0, 11, 1)
x_difuso = fuzz.trimf(x, [0, 5, 10])

# Evaluar la pertenencia difusa para un valor
valor = 3
pert_difusa = fuzz.interp_membership(x, x_difuso, valor)

print("Pertenencia difusa para el valor", valor, "es", pert_difusa)
