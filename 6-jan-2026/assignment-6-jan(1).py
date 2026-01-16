# Program to calculate total and average of 3 subjects

# Input marks for three subjects
s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))

# Calculate total
total = s1 + s2 + s3

# Calculate average
average = total / 3

# Display results
print("\n--- Results ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
