fahrenheit = [32, 68, 77, 104, 212]
print("Fahrenheit List:", fahrenheit)

celsius = []
for f in fahrenheit:
    c = (f - 32) * 5 / 9
    celsius.append(c)

print("Celsius List:", celsius)
