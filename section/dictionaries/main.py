# main.py

# 1. Definir el diccionario grocery_inventory con los ítems indicados
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# 2. Recuperar los detalles de "Bread" y guardarlos en bread_details
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)

# 3. Agregar "Cookies" con su ID y categoría
grocery_inventory.update({"Cookies": (143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)

# 4. Eliminar "Eggs" del inventario
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)