'''

# Original tuple
t = (10, 20, 30, 40, 50)

# Convert to list
temp = list(t)

# Delete element at index 2 (value 30)
del temp[2]

# Convert back to tuple
new_t = tuple(temp)

print("Original Tuple:", t)
print("After Deleting Element:", new_t)

'''

# Taking tuple elements from user
elements = input("Enter tuple elements separated by space: ")

# Convert input string to tuple
t = tuple(elements.split())

# Display original tuple
print("Original Tuple:", t)

# Ask user which index to delete
index = int(input("Enter the index of element to delete: "))

# Check if index is valid
if index >= 0 and index < len(t):
    # Create new tuple without the selected element
    new_t = t[:index] + t[index+1:]
    
    print("New Tuple after deletion:", new_t)
else:
    print("Invalid index!")
