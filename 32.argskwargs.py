# args are non keyword variable number of arguments and are passed on to function as tuple
# kwargs are keyword variable number of arguments (key value pair) and are passed on to function as dictionary

def my_func(*args):
    for i in args:
        print(i)
    print(args)


my_func(1, 2, 3, 4, 5, 6)


def my_func2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


my_func2(name="Saurabh", age=25, city="New York")
