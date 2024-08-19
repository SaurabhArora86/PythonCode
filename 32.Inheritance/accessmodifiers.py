# Default all attributes - variables and methods are public
class Employee:
    def __init__(self):
        self.name = "Saurabh"


e = Employee()
print(e.name)

# To make variables private


class Person:
    def __init__(self):
        # By using __variablename makes it private
        self.__name = "Saurabh"


e1 = Person()
# We cannot use below way to access name
# print(e1.name)
# However to access there is an option called as Name Mangling where in the syntax is _ClassName__variable
print(e1._Person__name)

'''
Python does mangling whenever there is __ i.e it makes the variable or function private
But there is no concept of Protected in Python
To follow a convention, you may use _variableName i.e single underscore before variable name to denote that it is protected but Python does nothing related to enforcing
It is just a naming convention that organization follows
PS: in OOPs Private means only accessible within class
    Public is default that it can be accessed outside the class
    Protected means it can be accessed within class or extended classes but not outside
'''
