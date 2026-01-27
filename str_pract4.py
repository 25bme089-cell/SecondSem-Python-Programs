# Program to print first, last and middle character (if length is odd)

str1 = input("Enter a string: ")

# First character
print("First character:", str1[0])

# Last character
print("Last character:", str1[-1])

# Middle character (only if length is odd)
length = len(str1)
if length % 2 != 0:  # odd length
    middle_index = length // 2
    print("Middle character:", str1[middle_index])
