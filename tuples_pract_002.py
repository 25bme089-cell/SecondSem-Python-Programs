students = [
    (1, "Rahul", 18),
    (2, "Anita", 19),
    (3, "Karan", 17),
    (4, "Sneha", 18)
]

roll_nos = []
names = []
ages = []

for roll, name, age in students:
    roll_nos.append(roll)
    names.append(name)
    ages.append(age)

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
