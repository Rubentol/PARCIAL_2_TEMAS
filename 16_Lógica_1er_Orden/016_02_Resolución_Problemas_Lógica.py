#Resolución de Problemas usando Lógica de Primer Orden

from sympy import solve, Eq
import numpy as np

# Crear una matriz de Sudoku como un problema de lógica de primer orden
sudoku_grid = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

# Definir símbolos como variables
symbols_dict = {(i, j): symbols(f"P_{i}_{j}") for i in range(9) for j in range(9)}

# Crear las reglas para el Sudoku usando lógica de primer orden
sudoku_rules = []
for i in range(9):
    for j in range(9):
        if sudoku_grid[i][j] != 0:
            sudoku_rules.append(Eq(symbols_dict[(i, j)], sudoku_grid[i][j]))
        
# Resolver el problema de Sudoku
solucion = solve(sudoku_rules)

# Mostrar la solución
for i in range(9):
    row = [solucion[symbols_dict[(i, j)]] for j in range(9)]
    print(row)
