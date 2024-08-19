'''
Decorators are used to modify a function
for eg: You have 20 functions and want a common modified behavior for all
Define common behavior in a decorator function and add a decorator on top of 20 function definitions

Decorators takes argument as a function and returns a function
@decorator_function
def normal_function():

'''


# Decorator function
def decorate_me(fx):
    def mfx():
        print("Hey Good Morning")
        fx()
    return mfx


@decorate_me
def add():
    print(10+2)


add()


def decorate_you(fx):
    # This is to take *args as tuple and **kwargs as dictionary for x arguments
    def mfx(*args):
        print("Hey Good Morning")
        fx(*args)
    return mfx


@decorate_you
def subtract(a, b, c):
    print(a-b-c)


subtract(10, 20, 30)
