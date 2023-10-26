#Extracción de Entidades Nominadas (NER)

import spacy

# Cargar el modelo de lenguaje en inglés
nlp = spacy.load("en_core_web_sm")

# Texto con entidades nominadas
texto = "Apple Inc. fue fundada por"
