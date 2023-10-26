#Modelos de Temas con Modelos de Asignación Latente (LDA)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Datos de texto
documents = [
    "Este es un documento sobre aprendizaje automático y lenguaje.",
    "El procesamiento del lenguaje natural es una rama importante de la inteligencia artificial.",
    "Los modelos de lenguaje probabilísticos son fundamentales en NLP."
]

# Vectorizar los documentos
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Aplicar LDA
num_topics = 2  # Número de temas
lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
lda.fit(X)

# Obtener palabras clave para cada tema
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(lda.components_):
    top_keywords_idx = topic.argsort()[-5:][::-1]  # Obtener las 5 palabras clave principales
    top_keywords = [feature_names[i] for i in top_keywords_idx]
    print(f"Tema {topic_idx + 1}: {', '.join(top_keywords)}")
