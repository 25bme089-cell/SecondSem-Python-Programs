import random

# Create list of 5 odd integers
odd_list = [random.randrange(1, 100, 2) for _ in range(5)]
print("Odd List:", odd_list)

# Create list of 4 even integers
even_list = [random.randrange(2, 100, 2) for _ in range(4)]
print("Even List:", even_list)

# Replace third element with even list
odd_list[2] = even_list
print("After replacing 3rd element:", odd_list)

# Flatten the list
flat_list = []
for item in odd_list:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

print("Flattened List:", flat_list)

# Sort the list
flat_list.sort()
print("Sorted List:", flat_list)
