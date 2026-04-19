def count_lower_upper(text):
    result = {
        "lowercase": 0,
        "uppercase": 0
    }
    
    for char in text:
        if char.islower():
            result["lowercase"] += 1
        elif char.isupper():
            result["uppercase"] += 1
    
    return result

sample = input("enter string under observation:")
output = count_lower_upper(sample)
print(output)
