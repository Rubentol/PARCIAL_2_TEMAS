#Algoritmo de A (A Star)*

import heapq

def astar(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)
        if current_node == goal:
            path = reconstruct_path(came_from, goal)
            return path

        for neighbor, weight in graph[current_node].items():
            tentative_g_score = g_score[current_node] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score + heuristic(neighbor, goal), neighbor))

    return None

def reconstruct_path(came_from, goal):
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    return path

def heuristic(node, goal):
    # Función heurística para estimar el costo futuro (puedes personalizarla según el problema)
    pass

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 4},
    'C': {'A': 3, 'D': 1},
    'D': {'B': 4, 'C': 1}
}
start = 'A'
goal = 'D'
print(astar(graph, start, goal))  # Output: ['A', 'B', 'D']