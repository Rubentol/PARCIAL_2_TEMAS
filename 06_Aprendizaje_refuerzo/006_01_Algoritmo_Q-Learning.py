#Algoritmo Q-Learning

import random

# Inicialización de la matriz Q con valores arbitrarios
Q = [[0 for _ in range(num_actions)] for _ in range(num_states)]

for _ in range(num_episodes):
    state = random.randint(0, num_states - 1)
    while not is_terminal(state):
        # Elegir una acción aleatoria o la mejor acción según la matriz Q
        action = select_action(state)
        next_state, reward = take_action(state, action)
        
        # Actualizar la matriz Q usando la fórmula de Q-Learning
        Q[state][action] = Q[state][action] + learning_rate * (reward + discount_factor * max(Q[next_state]) - Q[state][action])
        
        state = next_state

# Utilizar la matriz Q para tomar decisiones óptimas
current_state = start_state
while not is_terminal(current_state):
    action = select_best_action(current_state)
    next_state, _ = take_action(current_state, action)
    print(f"Move from state {current_state} to state {next_state}")
    current_state = next_state
