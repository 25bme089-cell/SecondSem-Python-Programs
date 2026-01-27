# Program to concatenate a string with itself multiple times

# Accept string from user
str1 = input("Enter a string: ")

# Accept number of times to repeat
n = int(input("Enter the number of times to concatenate: "))

# Concatenate manually (without using * operator)
result = ""
count = 0
while count < n:
    result += str1
    count += 1

print("Final concatenated string:", result)
