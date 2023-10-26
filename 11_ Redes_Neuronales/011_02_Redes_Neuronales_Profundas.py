#Redes Neuronales Profundas (Deep Neural Networks)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Definir la arquitectura de la red neuronal
model = Sequential([
    Dense(128, input_shape=(input_size,), activation='relu'),
    Dense(64, activation='relu'),
    Dense(output_size, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
