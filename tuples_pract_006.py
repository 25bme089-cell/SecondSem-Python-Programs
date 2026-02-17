# Original tuple
t = (10, 20, 30, 40)

# Convert to list to modify (since tuple is immutable)
temp = list(t)

# Modify element (change 30 to 300)
temp[2] = 300

# Convert back to tuple
new_t = tuple(temp)

print("Original Tuple:", t)
print("Modified Tuple:", new_t)
