#Política y Función de Valor

# Inicializar política y función de valor
policy = {state: random.choice(actions) for state in states}
value_function = {state: 0 for state in states}

# Iterar sobre la política
for _ in range(num_iterations):
    for state in states:
        action = policy[state]
        next_state, reward = take_action(state, action)
        # Actualizar la función de valor usando la ecuación de Bellman
        value_function[state] = reward + discount_factor * value_function[next_state]

# Iterar sobre la función de valor
for state, value in value_function.items():
    print(f"State: {state}, Value: {value}")
