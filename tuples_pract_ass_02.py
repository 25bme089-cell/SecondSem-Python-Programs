food_list = []

n = int(input("How many food items? "))

for i in range(n):
    name = input("Enter food name: ")
    price = float(input("Enter price: "))
    
    food_list.append((name, price))

print("\nOriginal List:")
print(food_list)

# Sorting by price in descending order
sorted_list = sorted(food_list, key=lambda x: x[1], reverse=True)

print("\nSorted List (Descending by Price):")
print(sorted_list)
