'''
When one child class inherits multiple parent class, it is called as Multiple Inheritance
eg: class A, class B, class C(A,B)
NOTE:
When one child class inherits another class, which in turn inherits another class, it is called Multilevel Inheritance
eg: class C(B), class B(A), class A
'''


class A:
    pass


class B:
    pass


class C(A, B):
    pass


'''
Here class C inherits Class A and Class B
'''
