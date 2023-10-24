#Teorema de Bayes
# Teorema de Bayes: P(A|B) = P(B|A) * P(A) / P(B)
probabilidad_b_dado_a = 0.9
probabilidad_a = 0.7
probabilidad_b = 0.8

probabilidad_a_dado_b = (probabilidad_b_dado_a * probabilidad_a) / probabilidad_b
print("Probabilidad de A dado B:", probabilidad_a_dado_b)
