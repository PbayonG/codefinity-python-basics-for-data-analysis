# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Iterar usando range para índices
for i in range(len(weekdays)):
    print(f"{weekdays[i]}: Promotion on {daily_promotions[i]}")