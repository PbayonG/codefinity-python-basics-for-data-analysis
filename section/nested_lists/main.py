# Task 1: Assign `vegetables` to a list of strings containing "tomatoes", "potatoes", and "onions"
vegetables = ["tomatoes", "potatoes", "onions"]

# Task 2: Remove "onions" from the list
vegetables.remove("onions")

# Task 3: Add "carrots" string to the list if it's not already present
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# Task 4: Check if "cucumbers" are in the list and add them if they're not
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# Task 5: Sort the list alphabetically
vegetables.sort()

# Print the updated and sorted vegetable list
print("Updated Vegetable Inventory:", vegetables)