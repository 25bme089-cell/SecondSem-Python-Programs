def series(z):
    l1=[]
    for i in range(1,z+1):
        t=(i,i*i,i*i*i)
        l1.append(t)
    return l1

num = int(input("Enter a number: "))
print(series(num))
    
