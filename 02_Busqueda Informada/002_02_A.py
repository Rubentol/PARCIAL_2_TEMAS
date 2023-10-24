#Búsqueda A*

def astar_search(graph, heuristic, start, goal):
    open_list = [(start, 0, heuristic[start])]
    closed_list = set()

    while open_list:
        current_node, cost, heuristic_value = min(open_list, key=lambda x: x[1] + x[2])
        open_list.remove((current_node, cost, heuristic_value))

        if current_node == goal:
            return True  # Se encontró una solución

        closed_list.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_list:
                new_cost = cost + 1
                heuristic_value = heuristic[neighbor]
                open_list.append((neighbor, new_cost, heuristic_value))

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
result = astar_search(graph, heuristic, start_node, goal_node)
print("¿Se encontró una solución?", result)
