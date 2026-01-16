# Program to calculate total and average of 3 subjects

# Input marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate total
total = subject1 + subject2 + subject3

# Calculate average
average = total / 3

# Display results
print("\n--- Results ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
