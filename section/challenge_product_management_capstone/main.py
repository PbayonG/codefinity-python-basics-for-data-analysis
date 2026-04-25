# Input variables
days_until_expiration = 5  # Example value
stock_level = 60           # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

# Determine the discount based on product type, days until expiration, and stock level
if product_type == "Perishable":
    # Aplicar 30% si faltan 3 días o menos y stock es mayor a 50
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    # Aplicar 20% si faltan entre 4 y 6 días y stock es mayor a 50
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    # Aplicar 10% si faltan 7 días o más o stock es 50 o menos
    elif days_until_expiration >= 7 or stock_level <= 50:
        print("10% discount applied")
else:
    # No aplicar descuento si no es perecedero
    print("No discount available for non-perishable items.")