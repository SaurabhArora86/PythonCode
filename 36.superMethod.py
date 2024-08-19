class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


class Programmer(Employee):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang

    def show(self):
        print(f"{self.name} has experience in {self.lang}")


c2 = Employee("Saurabh", 37)
c1 = Programmer("Saurabh", 37, "Python")
c1.show()
