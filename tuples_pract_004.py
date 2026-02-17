food_items = [
    ("Pizza", 250),
    ("Burger", 120),
    ("Pasta", 200),
    ("Sandwich", 80)
]

# Sort by price (index 1) in descending order
sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)

print("Sorted food items (descending by price):")
for item in sorted_items:
    print(item)
