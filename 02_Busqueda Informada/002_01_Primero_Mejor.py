#Búsqueda Primero el Mejor (Best-First Search) 

def best_first_search(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    closed_list = set()

    while open_list:
        current_node, _ = min(open_list, key=lambda x: x[1])
        open_list.remove((current_node, _))

        if current_node == goal:
            return True  # Se encontró una solución

        closed_list.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_list and neighbor not in [node[0] for node in open_list]:
                heuristic_value = heuristic[neighbor]
                open_list.append((neighbor, heuristic_value))

    return False  # No se encontró una solución

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {
    'A': 3,
    'B': 2,
    'C': 5,
    'D': 1,
    'E': 4,
    'F': 0
}
start_node = 'A'
goal_node = 'F'
result = best_first_search(graph, heuristic, start_node, goal_node)
print("¿Se encontró una solución?", result)
