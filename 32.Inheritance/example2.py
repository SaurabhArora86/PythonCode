# First letter of class is in Caps
import random


class Employee:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(1, 1000)

    def showName(self):
        print(f"Employee is {self.name} with ID {self.id}")


e1 = Employee("Saurabh")
e1.showName()


class Programmer(Employee):
    def __init__(self, name, language):
        # When you define an init in extended class, you need to call constructor of super class with super()__init__
        super().__init__(name)
        self.language = language

    def showLang(self):
        print(f"Default language is {self.language}")


e2 = Programmer("Deepak", "Python")
e2.showName()
e2.showLang()


class Age(Employee):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def showAge(self):
        print(f"Age is {self.age} with Name {self.name}")


e3 = Age("Saurabh", 36)
e3.showAge()
