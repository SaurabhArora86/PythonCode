# If global ariable values are to be changed inside a function, it is referenced with name "global"

x = 4


def Hello():
    # Here variable x is global and used in function so its value will be 4
    # print(x)
    # if value is to be changed, reference the variable as global variable
    global x
    x = 10
    print(x)
    y = 5
    print(y)


Hello()
# Below will give an error since y scope is within function and gets destroyed afterwords
# print(y)
