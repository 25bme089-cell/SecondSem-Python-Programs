'''

# Boys' names stored as tuples, girls' names as strings
names = [("Rahul",), "Anita", ("Karan",), "Sneha", ("Aman",), "Pooja"]

boys = 0
girls = 0

for ele in names:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)

'''

# Boys stored in one big tuple
names = [
    ("Rahul", "Karan", "Aman"),   # Boys (single big tuple)
    "Anita",
    "Sneha",
    "Pooja"
]

boys = 0
girls = 0

for ele in names:
    if isinstance(ele, tuple):
        boys += len(ele)   # Count number of boys inside tuple
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)
