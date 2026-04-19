# Accept two sets from user
set1 = set(input("Enter elements of first set (space separated): ").split())
set2 = set(input("Enter elements of second set (space separated): ").split())

# Check subset
print("First is subset of second:", set1.issubset(set2))

# Check superset
print("Second is superset of first:", set2.issuperset(set1))

# Check equality
print("Both sets are equal:", set1 == set2)
