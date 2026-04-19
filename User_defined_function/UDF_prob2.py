def compute(n):
    total = 0
    temp = ""
    
    for i in range(4):
        temp += str(n)
        total += int(temp)
    
    return total


for i in range(4, 8):
    print(i, "->", compute(i))
    
