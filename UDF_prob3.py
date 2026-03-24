def create_array(x,y,z,value):
    arr=[[[value for k in range(z)]
          for j in range(y)]
         for i in range(x)]
    return arr

a=create_array(3,4,5,7)
for i in range (len(a)):
    print(i+1)
for r in a[i]:
    print(r)
