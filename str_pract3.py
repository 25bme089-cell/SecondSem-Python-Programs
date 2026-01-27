# Program to access a string in forward and reverse directions using while loop

str1 = input("Enter a string: ")

# Forward direction
print("Forward direction:")
i = 0
while i < len(str1):
    print(str1[i], end=" ")
    i += 1

# Reverse direction
print("\nReverse direction:")
j = len(str1) - 1
while j >= 0:
    print(str1[j], end=" ")
    j -= 1
