# Program to calculate sin(x) using Taylor series expansion

import math

def sine_taylor(x, terms=10):
    # x is in radians
    result = 0
    for n in range(terms):
        sign = (-1)**n
        result += sign * (x**(2*n+1)) / math.factorial(2*n+1)
    return result

# Example usage:
x_deg = float(input("Enter angle in degrees: "))
x_rad = x_deg * math.pi / 180  # convert to radians
print(f"sin({x_deg}°) ≈ {sine_taylor(x_rad)}")
print(f"(Python math.sin gives: {math.sin(x_rad)})")