# Lista de precios de los productos
prices = [12.99, 8.50, 15.75, 23.00, 7.25]

# Inicializar total en 0
total = 0

# Sumar cada precio al total
for price in prices:
    total += price  # equivalente a total = total + price

# Mostrar el resultado final
print("Total price for products:", total)