# main.py

def apply_discount(prices):
    # Crear una copia de la lista original para no modificarla
    prices_copy = prices.copy()
    # Recorrer la copia usando índices
    for i in range(len(prices_copy)):
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.90  # Aplicar descuento del 10%
    return prices_copy

# Lista de precios de productos
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Llamar a la función y almacenar los precios actualizados
updated_prices = apply_discount(product_prices)

# Imprimir el resultado
print(f"Updated product prices: {updated_prices}")