# Recursive function to find length of string
def str_length(s):
    if s == "":
        return 0
    else:
        return 1 + str_length(s[1:])

# Example usage
text = "Hello"
print("Length of string:", str_length(text))
