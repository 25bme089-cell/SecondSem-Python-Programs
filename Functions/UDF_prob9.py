def count_alpha_digits(text):
    result = {
        "alphabets": 0,
        "numbers": 0
    }
    
    for char in text:
        if char.isalpha():
            result["alphabets"] += 1
        elif char.isdigit():
            result["numbers"] += 1
    
    return result


# Example usage
sample = input("Enter a string: ")
output = count_alpha_digits(sample)
print(output)
    
