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


class Company:
    compName = "Google"

    def companyName(self):
        print(f"Company name is {self.compName}")

    @classmethod
    def company_loc(cls):
        print(f"Location is Santa Maria")


class Employee:
    eName = "Saurabh"

    def empName(self):
        print(f"Employee name is {self.eName}")


class Code(Employee, Company):
    language = "Python"

    def codeLanguae(self):
        print(
            f"Language is {self.language} and Company name is {self.compName} and Employee name is {self.eName}")


a = Code()
a.compName = "Apple"
a.eName = "Saurabh"
a.companyName()
a.empName()
a.codeLanguae()
# Below will throw an error as companyName() takes self as an argument means it is expecting to be called with an instance not with class name
# If had to be called with class name remove self from companyName() method
# Company.companyName()
# Below is a clas method and can be called with class name, note we need to pass cls as an argument to it otherwise use static method
# as it is not making any changes to company properties so static method is better suited for this
Company.company_loc()
