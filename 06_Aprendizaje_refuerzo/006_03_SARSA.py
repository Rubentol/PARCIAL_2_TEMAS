#Algoritmo SARSA (State-Action-Reward-State-Action)

# Inicialización de la matriz Q con valores arbitrarios
Q = [[0 for _ in range(num_actions)] for _ in range(num_states)]

for _ in range(num_episodes):
    state = random.randint(0, num_states - 1)
    action = select_action(state)
    while not is_terminal(state):
        next_state, reward = take_action(state, action)
        next_action = select_action(next_state)
        
        # Actualizar la matriz Q usando la fórmula de SARSA
        Q[state][action] = Q[state][action] + learning_rate * (reward + discount_factor * Q[next_state][next_action] - Q[state][action])
        
        state, action = next_state, next_action
