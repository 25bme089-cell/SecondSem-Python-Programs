# Program to create new file without "a", "an", "the"

# Open original file
with open("input.txt", "r") as f1:
    words = f1.read().split()

# Filter out unwanted words
filtered = [w for w in words if w.lower() not in ["a", "an", "the"]]

# Write to new file
with open("output.txt", "w") as f2:
    f2.write(" ".join(filtered))

print("New file created without 'a', 'an', 'the'.")
