'''
Decorators are used to modify a function
for eg: You have 20 functions and want a common modified behavior for all
Define common behavior in a decorator function and add a decorator on top of 20 function definitions

Decorators takes argument as a function and returns a function
@decorator_function
def normal_function():

'''

'''
Dacorators are used to modify an existing function, they take argument as original function and returns the mofiied function

def dacorator_function(original_function):
    def wrapper():
        print("I am executed before the original function")
        return original_function()
    return wrapper

@dacorator_function
def display():
    print("I am the original function")

display()

Outcome:
I am exucuted before the original function
I am the original function

Steps:
1. when you call original_function, original_function is passed to dacorator_function
2. dacorator_function returns wrapper which is now associated with display rather than original_function
3. When display() is called, wrapper function is executed first and then calls the original_function
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
        return fx(*args)
    return mfx


@decorate_you
def subtract(a, b, c):
    print(a-b-c)


subtract(10, 20, 30)
