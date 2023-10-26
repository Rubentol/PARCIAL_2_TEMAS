#Perceptrón y Redes Neuronales Básicas

import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0

    def train(self, inputs, labels):
        for _ in range(self.epochs):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                self.weights[1:] += self.learning_rate * (labels[i] - prediction) * inputs[i]
                self.weights[0] += self.learning_rate * (labels[i] - prediction)
