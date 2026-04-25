# main.py

produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# Combina las dos listas en una lista de listas
groceries = [produce, dairy]

# Usa bucles anidados para imprimir cada ítem
for section in groceries:
    for item in section:
        print("Item name:", item)