def convert(s):
    s = s.replace(" ", "")      # remove spaces
    unique_chars = set(s)       # remove duplicates
    sorted_chars = sorted(unique_chars, key=lambda x: (not x.isdigit(), x.lower()))
    return ''.join(sorted_chars)

# input
str1 = input("Enter a string: ")
result = convert(str1)

print("Converted string:", result)
