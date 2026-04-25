# Inicializar listas de la charcutería
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Crear la lista principal y mostrar el estado inicial
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)

# Repoblar "Ham" si su cantidad es menor de 100
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

# Añadir carne de temporada y eliminar el condimento
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)

# Ordenar alfabéticamente por el primer elemento de cada sublista
deli_dept.sort()

# Mostrar el estado actualizado
print("Updated Deli List:", deli_dept)