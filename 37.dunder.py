# Dunder methods have __methodname__ and are used to do special things like example below

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        j = 0
        for i in self.name:
            j += 1
        return j

    def __str__(self):
        return (f"Name is {self.name}")


c1 = Employee("Saurabh")
# After adding __len__ we can get len(object)
print(len(c1))
# Here once we have added __str__ dunder method, we can get c1 object printed rather than usual print(c1) which gives memory location
print(c1)
print(str(c1))
