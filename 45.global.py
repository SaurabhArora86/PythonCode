# Scope if a variable defined in function is limited to fucntion itself

def fun():
    a = 10
    print(a)


fun()

try:
    print(a)
except:
    print("a is not defined")


b = 90
# SInce b is changed within function, outside the function, its value changes back to 90


def fun2():
    b = 10
    print(b)


fun2()
print(b)


c = 6


def fun3():
    global c
    c = 100
    print(c)


fun3()
print(c)
