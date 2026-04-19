# Program to generate N Fibonacci numbers

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
N = int(input("Enter how many Fibonacci numbers: "))
print(f"Fibonacci series ({N} terms):", fibonacci(N))