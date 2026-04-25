# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slice the `items` string into individual items
candy1    = items[:9]     # Bubblegum
candy2    = items[11:20]  # Chocolate
dry_goods = items[22:]    # Pasta

# Slice the `categories` string into individual categories
category1 = categories[:11]  # Candy Aisle
category2 = categories[13:]  # Pasta Aisle

# Define the prices for each item
bubblegum_price  = "$1.50"  # Bubblegum costs 1.50 dollars
chocolate_price  = "$2.00"  # Chocolate costs 2.00 dollars
pasta_price      = "$5.40"  # Pasta costs 5.40 dollars

# Print formatted statements combining items, prices, and categories
print("We have " + candy1 + " for " + bubblegum_price + " in the " + category1)
print("We have " + candy2 + " for " + chocolate_price + " in the " + category1)
print("We have " + dry_goods + " for " + pasta_price + " in the " + category2)