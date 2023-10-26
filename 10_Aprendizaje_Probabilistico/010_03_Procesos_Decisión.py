#Procesos de Decisión de Markov

import numpy as np

# Inicializar valores de utilidad y recompensas
n_states = 5
n_actions = 3
discount_factor = 0.9
rewards = np.array([0, 0, 0, 1, -1])

# Inicializar valores de utilidad arbitrarios
utilities = np.zeros(n_states)

# Definir la función de evaluación de política
def policy_evaluation(utilities, rewards, transition_probs, discount_factor, num_iterations=100):
    for _ in range(num_iterations):
        for state in range(n_states):
            expected_rewards = [sum(transition_probs[state, action, new_state] * (rewards[new_state] + discount_factor * utilities[new_state]) 
                                for new_state in range(n_states))
                                for action in range(n_actions)]
            utilities[state] = max(expected_rewards)
    return utilities

# Suponiendo que tienes matrices de transición transition_probs
# Llamar a la función de evaluación de política
estimated_utilities = policy_evaluation(utilities, rewards, transition_probs, discount_factor)
print("Utilidades estimadas después de la evaluación de política:", estimated_utilities)
