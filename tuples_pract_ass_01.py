from datetime import date

# Taking first date
d1 = int(input("Enter day of first date: "))
m1 = int(input("Enter month of first date: "))
y1 = int(input("Enter year of first date: "))

# Taking second date
d2 = int(input("Enter day of second date: "))
m2 = int(input("Enter month of second date: "))
y2 = int(input("Enter year of second date: "))

# Creating date tuples
date1 = (d1, m1, y1)
date2 = (d2, m2, y2)

print("First Date Tuple:", date1)
print("Second Date Tuple:", date2)

# Converting tuple to date object
dt1 = date(y1, m1, d1)
dt2 = date(y2, m2, d2)

# Finding difference
difference = abs((dt2 - dt1).days)

print("Number of days between two dates:", difference)
