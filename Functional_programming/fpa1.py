# Define three simple functions
def f1():
    print("Function 1")

def f2():
    print("Function 2")

def f3():
    print("Function 3")

# Store them in a list
funcs = [f1, f2, f3]

# Call each in a loop
for fn in funcs:
    fn()
