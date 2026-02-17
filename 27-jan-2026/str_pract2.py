# 65–90 for uppercase (A-Z) and 97–122 for lowercase (a-z)

# Program to display Toggle Case, Lowercase, and Uppercase
# without using built-in string functions

str1 = input("Enter a string: ")

toggle_result = ""
lower_result = ""
upper_result = ""

for c in str1:
    ascii_val = ord(c)

    # Toggle case
    if 65 <= ascii_val <= 90:  # Uppercase A-Z
        toggle_result += chr(ascii_val + 32)  # convert to lowercase
    elif 97 <= ascii_val <= 122:  # Lowercase a-z
        toggle_result += chr(ascii_val - 32)  # convert to uppercase
    else:
        toggle_result += c  # keep non-alphabet characters unchanged

    # Lowercase conversion
    if 65 <= ascii_val <= 90:  # Uppercase A-Z
        lower_result += chr(ascii_val + 32)
    else:
        lower_result += c

    # Uppercase conversion
    if 97 <= ascii_val <= 122:  # Lowercase a-z
        upper_result += chr(ascii_val - 32)
    else:
        upper_result += c

print("\nResults:")
print("Toggle Case :", toggle_result)
print("Lowercase   :", lower_result)
print("Uppercase   :", upper_result)

