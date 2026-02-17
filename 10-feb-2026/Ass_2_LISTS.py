list1 = [10, 20, 30, 40, 50]
list2 = [30, 50, 70]

result = [x for x in list1 if x not in list2]

print("First List:", list1)
print("Second List:", list2)
print("Elements not in second list:", result)
