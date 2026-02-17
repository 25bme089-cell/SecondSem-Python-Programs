from datetime import date

# Date tuples (d, m, y)
date1 = (7, 9, 2006)
date2 = (17, 2, 2026)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

difference = abs((d2 - d1).days)

print("Number of days between two dates:", difference)
