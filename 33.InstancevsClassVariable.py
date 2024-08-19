# 1. Variables defined within constructor are instance variables
# 2. Variables defined at class level is class variables
# 3. If instance variable and class variable both exists then Instance variable superseeds
# 4. Class variable remains common across all instances unless Instance variable superseeds it with overiding
# 5. Class variables are called using class name followed by variable name

class Employee:
    # Point 2
    companyName = "Apple"
    noOfEmployees = 0

    def __init__(self, name):
        # Point 1
        self.name = name
        self.raise_amount = 0.2
        # Point 5
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(f'Company Name is {self.companyName} and Employee name is {
              self.name} with raise is {self.raise_amount}, total employee strength is {Employee.noOfEmployees}')


e1 = Employee("Saurabh")
e1.showDetails()
# Point 3
e1.companyName = "Google"
e1.raise_amount = 0.3
e1.showDetails()

e1 = Employee("Rohan")
e1.showDetails()
