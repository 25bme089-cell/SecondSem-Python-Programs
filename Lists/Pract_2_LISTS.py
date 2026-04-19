import random

nums = [random.randint(1, 20) for _ in range(20)]
print("List:", nums)

n = int(input("Enter number to search: "))

positions = []
for i, val in enumerate(nums):
    if val == n:
        positions.append(i)

if positions:
    print("Number found at positions:", positions)
else:
    print("Number not found in list")
