# superMethod is used to call the parent class method from the child class
# Syntax : super().__init__(args)
'''
class ABC:
    def __init__(self,name):
        self.name = name
        print(self.name)
class XYZ(ABC):
    def __init__(self,age):
    super().__init__(name)
    self.age = age
    print(self.age)
'''


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


class Programmer(Employee):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang
        print(self.name, self.age, self.lang)

    def show(self):
        print(f"{self.name} has experience in {self.lang}")


c2 = Employee("Saurabh", 37)
c1 = Programmer("Saurabh", 37, "Python")
c1.show()


class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display(self):
        print(f"{self.name} manages the {self.department} department")


c3 = Manager("Saurabh", 37, "IT")
c3.display()


class Location(Employee):
    def __init__(self, location):
        self.location = location

    def call(self, name, age):
        super().__init__(name, age)
        print(self.location)


l1 = Location("New York")
l1.call("Saurabh", 37)
