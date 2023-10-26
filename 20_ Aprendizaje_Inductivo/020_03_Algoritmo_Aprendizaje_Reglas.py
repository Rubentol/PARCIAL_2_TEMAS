#Algoritmo de Aprendizaje por Reglas

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Datos de transacciones (por ejemplo, compras de clientes)
transactions = [['pan', 'leche', 'huevos'],
                ['leche', 'carne', 'pan', 'cerveza'],
                ['pan', 'leche', 'huevos', 'carne'],
                ['leche', 'huevos', 'cerveza'],
                ['pan', 'leche', 'huevos']]

# Convertir las transacciones en un formato adecuado para Apriori
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)

# Crear un DataFrame de transacciones binarias
df = pd.DataFrame(te_ary, columns=te.columns_)

# Aplicar el algoritmo Apriori para encontrar reglas frecuentes
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# Generar reglas de asociación a partir de los itemsets frecuentes
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print("Reglas de asociación:")
print(rules)
