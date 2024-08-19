def square(n):
    '''Takes a values and prints the square of that function'''
    print(n**2)


square(10)
# Below is how to print the docstring
# docstring gets a special treatement from Python Interpreter where it is not ignored
# It comes just after definition start of function, method, class or Object

print(square.__doc__)

# PEP8 is Python enhancement proposal that came in 2001 that tells
# best practices on writing Python code
