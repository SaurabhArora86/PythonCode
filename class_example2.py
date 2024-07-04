class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def my_func(self):
        print(f'Hello, My name is {self.first_name} {self.last_name}')

    # __str__() this function returns the values in class

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')


person1 = Name("John", "Cena")

print(person1.first_name)

print(person1.my_func())

print(person1)
