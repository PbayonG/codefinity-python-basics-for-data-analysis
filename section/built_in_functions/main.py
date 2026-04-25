# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

# Lista para almacenar las ventas totales de cada producto
total_sales_list = []

# 1. Iterar sobre el diccionario y calcular ventas totales
for product, values in products.items():
    # 2. Convertir precio a float y cantidad vendida a int
    price = float(values[0])
    quantity_sold = int(values[1])
    
    # Calcular las ventas totales para el producto actual
    total_sales = price * quantity_sold
    
    # Imprimir ventas totales para el producto
    print(f"Total sales for {product}: ${total_sales}")
    
    # 3. Agregar las ventas totales a la lista
    total_sales_list.append(total_sales)

# 4. Calcular e imprimir la suma total de todas las ventas
total_sum = sum(total_sales_list)
print(f"\nTotal sum of all sales: ${total_sum}")

# 5. Encontrar e imprimir las ventas mínima y máxima
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")