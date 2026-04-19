vow = {'a','e','i','o','u','A','E','I','O','U'}

s = input("Enter a string: ")
ayan = 0

for p in s:
    if p in vow:
        ayan+=1
    
print(ayan)
