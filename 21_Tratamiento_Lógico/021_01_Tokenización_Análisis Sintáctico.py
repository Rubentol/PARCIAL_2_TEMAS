#Tokenización y Análisis Sintáctico

import spacy

# Cargar el modelo de lenguaje en español
nlp = spacy.load("es_core_news_sm")

# Oración para analizar
oracion = "El gato está en la alfombra."

# Tokenización y análisis sintáctico
doc = nlp(oracion)

# Obtener tokens y sus funciones gramaticales
tokens = [token.text for token in doc]
funciones_gramaticales = [token.pos_ for token in doc]

print("Tokens:", tokens)
print("Funciones Gramaticales:", funciones_gramaticales)
