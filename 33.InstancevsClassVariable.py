# 1. Variables defined within constructor are instance variables
# 2. Variables defined at class level is class variables
# 3. If instance variable and class variable both exists then Instance variable superseeds
# 4. Class variable remains common across all instances unless Instance variable superseeds it with overiding
# 5. Class variables are called using class name followed by variable name
# 6. Class variables can also be called using instance name followed by variable name

class Employee:
    # Point 2
    companyName = "Apple"  # Class variable
    noOfEmployees = 0  # Class variable

    def __init__(self, name):
        # Point 1
        self.name = name  # Instance variable
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

e2 = Employee("Rohan")
e2.showDetails()  # noOfEmployees is incrementing by 1 with each instance creation

# New instance attribute can be created on the fly
e1.place = "Bangalore"  # Instance variable
print(e1.place)
# e1.homeway()        # This will throw error as homeway is not defined
# Note instance variables can be created on the fly but class variables cannot be created on the fly
# Instance ariables can be created on the fly but instance methods cannot be created on the fly
