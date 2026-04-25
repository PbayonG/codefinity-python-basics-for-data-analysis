# main.py

# Define a function to apply a discount with a default discount value of 5%
def apply_discount(price, discount=0.05):
    return price * (1 - discount)

# Define a function to apply tax with a default tax rate of 7%
def apply_tax(price, tax=0.07):
    return price * (1 + tax)

# Define a function to calculate the total price by applying both discount and tax
def calculate_total(price, discount=0.05, tax=0.07):
    # Aplica el descuento primero
    discounted_price = apply_discount(price, discount)
    # Luego aplica el impuesto al precio descontado
    final_price = apply_tax(discounted_price, tax)
    return final_price

# Llamada usando los valores por defecto
total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

# Llamada usando valores personalizados vía keyword arguments
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")