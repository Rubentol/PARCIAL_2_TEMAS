#Algoritmo de Algoritmo Genético

import random

def generate_random_solution(length):
    return [random.randint(0, 1) for _ in range(length)]

def fitness(solution, target):
    return sum([1 for bit, target_bit in zip(solution, target) if bit == target_bit])

def crossover(parent1, parent2):
    split_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    return child1, child2

def mutate(solution, mutation_rate):
    mutated_solution = []
    for bit in solution:
        if random.random() < mutation_rate:
            mutated_solution.append(1 - bit)  # Cambiar el bit si se cumple la tasa de mutación
        else:
            mutated_solution.append(bit)
    return mutated_solution

def genetic_algorithm(target, population_size, mutation_rate, generations):
    solution_length = len(target)
    population = [generate_random_solution(solution_length) for _ in range(population_size)]

    for generation in range(generations):
        # Evaluar la aptitud de cada individuo en la población
        fitness_scores = [fitness(solution, target) for solution in population]
        best_solution = population[fitness_scores.index(max(fitness_scores))]
        
        # Si hemos encontrado una solución perfecta, terminar el algoritmo
        if max(fitness_scores) == solution_length:
            return best_solution
        
        # Seleccionar padres para la reproducción (torneo)
        parents = []
        for _ in range(population_size // 2):
            tournament = random.sample(list(enumerate(fitness_scores)), 2)
            parent1 = tournament[0][0]
            parent2 = tournament[1][0]
            parents.append((population[parent1], population[parent2]))
        
        # Cruzar los padres para crear hijos
        children = []
        for parent1, parent2 in parents:
            child1, child2 = crossover(parent1, parent2)
            children.append(mutate(child1, mutation_rate))
            children.append(mutate(child2, mutation_rate))
        
        # Reemplazar la población actual con los hijos
        population = children

    # Si no se encuentra una solución perfecta, devolver la mejor solución encontrada
    return best_solution

# Ejemplo de uso
target_solution = [1, 0, 1, 1, 0, 1, 0, 1]
population_size = 100
mutation_rate = 0.1
generations = 1000
result = genetic_algorithm(target_solution, population_size, mutation_rate, generations)
print("Solución encontrada:", result)
