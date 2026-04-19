# Program to swap two numbers
# Demonstrates both methods: using a temporary variable and without using one

# Input two numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\nOriginal values:")
print(f"a = {a}, b = {b}")

# --- Method 1: Using a temporary variable ---
temp = a
a = b
b = temp

print("\nAfter swapping (using temp variable):")
print(f"a = {a}, b = {b}")

# Reset values for demonstration
a = int(input("\nRe-enter first number (a): "))
b = int(input("Re-enter second number (b): "))

print("\nOriginal values:")
print(f"a = {a}, b = {b}")

# --- Method 2: Without using a temporary variable ---
a = a + b
b = a - b
a = a - b

print("\nAfter swapping (without temp variable):")
print(f"a = {a}, b = {b}")