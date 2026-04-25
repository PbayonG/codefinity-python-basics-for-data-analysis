# Datos iniciales del artículo
seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Paso 1: Determinar riesgo de sobrestock
overstock_risk = seasonal and current_stock > high_stock_threshold

# Paso 2: Determinar elegibilidad para descuento
discount_eligible = not selling_well and not on_sale

# Paso 3: Decidir si aplicar descuento
make_discount = overstock_risk or discount_eligible

# Salida
print("Should the item be discounted?", make_discount)