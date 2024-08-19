def greet_user(name):
    print(f"Hi {name}")
    print("Welcome abord")


greet_user("John")

# Positional and keyword argument
# In function definition, it is called as parameters and in function call, it is called as arguments


def greet_user2(first_name, second_name):
    print(f"Hi {first_name} {second_name}")
    print("Welcome abord")


# "John" is a postional argument and second_name="Smith" is a keyword argument

greet_user2("John", second_name="Smith")


def my_func(list_val):
    for items in list_val:
        print(items)


my_func(["v1", "v2"])

# Another function


def func1(first_name, middle_name, last_name):
    print(first_name, middle_name, last_name)
    print(first_name + middle_name + last_name)
    print("My name is: ", first_name, middle_name, last_name)


func1("Saurabh", last_name="Arora", middle_name="No_Name")


# Default Arguments

def average(a=10, b=4):  # These are default arguments
    print("Aerage is", (a+b)/2)


average(5)
average(b=3)
average()

# Variable length/ Arbitrary Argument
# Average of x numbers


def average(*numbers):  # Here numbers is of variable length and is a tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    return (sum/len(numbers))


print(average(10, 10, 20, 30))

# Arbitrary param as dictionary


def name(**name):  # Here numbers is of variable length and is a tuple
    print("Hello ", name["fname"], name["secondname"], name["lastname"])


name(fname="Saurabh", secondname="Nothing", lastname="Arora")
