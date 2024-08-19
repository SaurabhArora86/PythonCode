# First way below

# import math

# print(math.sqrt(9))

# Second way to import specific functions and use it without . notation

# from math import sqrt
# print(sqrt(9))

# To import everything but not a recommended approach
# from math import *
# print(sqrt(9))


# Another option for shorthand

# import math as m
# print(m.sqrt(9))

# To import fucntion from another file in same directory
# PS: It is giving a lot of output since when you imported another file/module, it runs the entire file/module when a function from that file is called
# That is why usually in standard modules, there is no execuion of function
# Eg below

# from functions import greet_user
# print(greet_user("l"))

# To overcome it, use if __name__ == "main" in imported module
# Eg below
import saurabh
saurabh.greet("Saurabh")
