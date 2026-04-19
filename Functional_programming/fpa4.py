import random

numbers = [random.randint(-15, 15) for _ in range(10)]
print("Random numbers:", numbers)

# Using the numbers from above
squares = [n**2 for n in numbers]
print("Squares:", squares)
