# Lista de precios de productos
prices = [29.99, 45.50, 12.75, 38.20]

# Iterar usando índices para aplicar descuentos según posición
for i in range(len(prices)):
    if i == 0:
        prices[i] *= 0.90  # 10% de descuento
    elif i == 1:
        prices[i] *= 0.80  # 20% de descuento
    elif i == 2:
        prices[i] *= 0.85  # 15% de descuento
    elif i == 3:
        prices[i] *= 0.95  # 5% de descuento

    print(f"Updated price for item {i}: ${prices[i]:.2f}")