# Program to extract parts of a string and reverse it

str1 = "PDEU College"

# Split into words
words = str1.split()

# Extract PDEU (first word)
part1 = words[0]

# Extract College (second word)
part2 = words[1]

# Extract U Col (last char of first word + first 3 chars of second word)
part3 = words[0][-1] + " " + words[1][:3]

# Reverse the whole string
reversed_str = str1[::-1]

# Display results
print("Original string :", str1)
print("Extracted PDEU  :", part1)
print("Extracted College:", part2)
print("Extracted U Col :", part3)
print("Reversed string :", reversed_str)
