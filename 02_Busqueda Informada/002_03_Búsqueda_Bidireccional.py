#Búsqueda Bidireccional 

def bidirectional_search(graph, start, goal):
    forward_queue = [start]
    backward_queue = [goal]
    forward_visited = {start}
    backward_visited = {goal}

    while forward_queue and backward_queue:
        # Exploración desde el nodo inicial
        current_forward = forward_queue.pop(0)
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)
                forward_visited.add(neighbor)

            if neighbor in backward_visited:
                return True  # Se encontró una solución

        # Exploración desde el nodo final
        current_backward = backward_queue.pop(0)
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)
                backward_visited.add(neighbor)

            if neighbor in forward_visited:
                return True  # Se encontró una solución

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
start_node = 'A'
goal_node = 'B'
result = bidirectional_search(graph, start_node, goal_node)
print("¿Se encontró una solución?", result)
