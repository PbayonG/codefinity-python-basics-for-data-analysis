# Definición de la función para calcular el costo total
def calculate_total_cost(price, quantity):
    total_cost = price * quantity
    return total_cost

# Llamada a la función y muestra del resultado
apples_total_cost = calculate_total_cost(1.50, 10)
print(f"The total cost for apples is ${apples_total_cost}")