# Shopping billing system
prices = []
i = 0

while i < 5:
    try:
        value = float(input("Enter price of item: "))
        if value < 0:
            raise ValueError("Invalid price entered")
        prices.append(value)
        i += 1
    except ValueError as ve:
        print(ve)
    except Exception:
        print("Please enter a valid number")

# Calculate totals
total = sum(prices)
gst = total * 0.18
final = total + gst

print("Total Bill:", total)
print("GST (18%):", gst)
print("Final Payable Amount:", final)
