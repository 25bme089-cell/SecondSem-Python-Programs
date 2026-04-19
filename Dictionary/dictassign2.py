# Example dictionaries
sales1 = {'P001': 100, 'P002': 200, 'P003': 150}
sales2 = {'P002': 300, 'P004': 400}

# Merge dictionaries and add sales if product exists in both
merged_sales = sales1.copy()
for product, amount in sales2.items():
    merged_sales[product] = merged_sales.get(product, 0) + amount

# Display merged dictionary
print("Merged Sales Dictionary:", merged_sales)

# Find product with highest sale
max_product = max(merged_sales, key=merged_sales.get)
print("Product with Highest Sale:", max_product, "=", merged_sales[max_product])

# Sort dictionary by values in descending order
sorted_sales = dict(sorted(merged_sales.items(), key=lambda x: x[1], reverse=True))
print("Sorted Sales Dictionary:", sorted_sales)
