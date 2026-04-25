grocery_item = "Grilled Chicken Salad"

# Utiliza len() para obtener la longitud de la cadena
length_of_item = len(grocery_item)

# Índices positivos para el primer carácter de cada palabra
first_char = grocery_item[0]    # 'G' de "Grilled"
second_char = grocery_item[8]   # 'C' de "Chicken"
third_char = grocery_item[16]   # 'S' de "Salad"

# Índices negativos para el último carácter de cada palabra
last_char1 = grocery_item[-1]   # 'd' de "Salad"
last_char2 = grocery_item[-7]   # 'n' de "Chicken"
last_char3 = grocery_item[-15]  # 'd' de "Grilled"

# Pruebas
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)