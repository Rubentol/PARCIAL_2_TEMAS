#Teorema de Bayes y Clasificación Bayesiana

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Suponiendo que tienes datos en X_train, X_test, y etiquetas en y_train, y_test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador Naive Bayes
naive_bayes_classifier = GaussianNB()

# Entrenar el clasificador
naive_bayes_classifier.fit(X_train, y_train)

# Predecir las etiquetas para los datos de prueba
y_pred = naive_bayes_classifier.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo Naive Bayes: {:.2f}".format(accuracy))
