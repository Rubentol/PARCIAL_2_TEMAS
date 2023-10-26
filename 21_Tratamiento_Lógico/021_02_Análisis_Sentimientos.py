#Análisis de Sentimientos

from textblob import TextBlob

# Texto para análisis de sentimientos
texto = "Estoy muy feliz de aprender procesamiento de lenguaje natural."

# Crear un objeto TextBlob
blob = TextBlob(texto)

# Realizar análisis de sentimientos
sentimiento = blob.sentiment

print("Polaridad del Sentimiento:", sentimiento.polarity)
print("Subjetividad del Sentimiento:", sentimiento.subjectivity)
