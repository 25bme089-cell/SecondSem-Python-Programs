# Program to accept marks of 3 subjects and assign grades

def grade(marks):
    if marks == "Absent":
        return "NA"
    marks = int(marks)
    if 0 <= marks <= 39: return "F"
    elif 40 <= marks <= 44: return "P"
    elif 45 <= marks <= 49: return "C"
    elif 50 <= marks <= 54: return "B"
    elif 55 <= marks <= 59: return "B+"
    elif 60 <= marks <= 69: return "A"
    elif 70 <= marks <= 79: return "A+"
    elif 80 <= marks <= 100: return "O"
    else: return "Invalid"

marks = []
for i in range(3):
    m = input("Enter marks for subject " + str(i+1) + " (or type Absent): ")
    marks.append(m)

# Check pass/fail
fail = False
total = 0
count = 0
for m in marks:
    if m == "Absent":
        fail = True
    else:
        m = int(m)
        if m <= 39:
            fail = True
        total += m
        count += 1

average = total / count if count > 0 else 0

print("Total:", total)
print("Average:", average)
print("Result:", "Fail" if fail else "Pass")

# Subject-wise grades
for i in range(3):
    print("Subject", i+1, "Grade:", grade(marks[i]))
