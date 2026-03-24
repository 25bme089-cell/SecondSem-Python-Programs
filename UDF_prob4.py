def sum_avg():
    total = 0
    
    for i in range(5):
        marks = int(input("Enter marks: "))
        total += marks
    
    avg = total / 5
    
    print("Sum =", total)
    print("Average =", avg)


sum_avg()
