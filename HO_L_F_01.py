def fun():
    print("function 1 initiated")
def disp():
    print("function 2 initiated")
def msg():
    print("function 3 initiated")

lst_fn=[fun, disp, msg]

for gr in lst_fn:
    gr()
