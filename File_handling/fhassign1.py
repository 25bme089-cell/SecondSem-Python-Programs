# Program to copy contents of one file to another
# while converting lowercase to uppercase

# Open source file in read mode
with open("source.txt", "r") as f1:
    data = f1.read()

# Convert to uppercase
data = data.upper()

# Write to destination file
with open("destination.txt", "w") as f2:
    f2.write(data)

print("File copied with uppercase conversion.")
