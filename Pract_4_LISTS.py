import random

nums = [random.randint(-50, 50) for _ in range(30)]
print("Original List:", nums)

positive = []
negative = []

for n in nums:
    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)

print("Positive Numbers:", positive)
print("Negative Numbers:", negative)
