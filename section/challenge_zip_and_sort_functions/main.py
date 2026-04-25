# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Tarea 1: Combinar las tres listas en una lista de tuplas
combined_list = list(zip(products, prices, quantities_sold))

# Tarea 2: Ordenar la lista combinada por nombre de producto
sorted_products = sorted(combined_list)

# Tarea 3: Imprimir cada producto en el formato requerido
for name, price, qty in sorted_products:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {qty}")