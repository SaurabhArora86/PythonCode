class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        return (f'"Your name is {self.fname} {self.lname}"')


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year


p1 = Student("John", "Cena", 24)

print(p1.graduation_year)

print(p1.print_name())
