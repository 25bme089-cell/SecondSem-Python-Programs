# List containing tuples (including empty tuples)
data = [(1, 2), (), (3, 4), (), (5,), ()]

# Remove empty tuples
new_data = [t for t in data if t != ()]

print("Original List:", data)
print("After Removing Empty Tuples:", new_data)
