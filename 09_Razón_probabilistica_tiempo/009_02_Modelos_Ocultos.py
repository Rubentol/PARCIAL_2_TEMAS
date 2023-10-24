#Modelos Ocultos de Markov (HMM)

from hmmlearn import hmm

# Definir el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=2)

# Secuencia de observaciones
observaciones = np.array([[0, 1, 0, 1, 0]]).T

# Ajustar el modelo al conjunto de datos
modelo_hmm.fit(observaciones)

# Predecir el estado oculto
estados_ocultos = modelo_hmm.predict(observaciones)

print("Secuencia de Estados Ocultos:", estados_ocultos)
