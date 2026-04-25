# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# 1. Convertir la lista de nuevos artículos en una tupla
shelf1_update_tuple = tuple(shelf1_update)

# 2. Concatenar la tupla nueva con la existente
shelf1_concat = shelf1 + shelf1_update_tuple

# 3. Contar cuántas veces aparece "celery"
celery_count = shelf1_concat.count("celery")

# 4. Encontrar el índice de la primera aparición de "celery"
celery_index = shelf1_concat.index("celery")

# Mostrar resultados
print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)