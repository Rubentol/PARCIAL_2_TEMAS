#Modelos de Lenguaje Probabilísticos

from collections import Counter
import nltk
from nltk.util import ngrams

# Tokenizar el texto en palabras
text = "Este es un ejemplo de texto de entrenamiento para el modelo de n-gramas."
words = nltk.word_tokenize(text)

# Crear n-gramas
n = 3  # Tamaño del n-grama
ngrams_list = list(ngrams(words, n))

# Contar la frecuencia de los n-gramas
ngram_freq = Counter(ngrams_list)

# Calcular probabilidades
total_ngrams = len(ngrams_list)
probabilities = {ngram: count / total_ngrams for ngram, count in ngram_freq.items()}
print("Probabilidades de los n-gramas:", probabilities)
