#Modelos Ocultos de Markov (HMM) para el Lenguaje

import nltk
from nltk.tag import hmm

# Obtener datos de entrenamiento para el modelo HMM
train_data = nltk.corpus.treebank.tagged_sents()[:3000]

# Entrenar un modelo HMM para el etiquetado de POS
tagger = hmm.HiddenMarkovModelTrainer().train(train_data)

# Etiquetar nuevas oraciones
sentence = "This is a simple POS tagging example."
tokens = nltk.word_tokenize(sentence)
pos_tags = tagger.tag(tokens)

print("Etiquetas POS para la oración:", pos_tags)
