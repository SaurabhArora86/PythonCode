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


def func1(first_name, middle_name, last_name):
    print(first_name, middle_name, last_name)
    print(first_name + middle_name + last_name)
    print("My name is: ", first_name, middle_name, last_name)


func1("Saurabh", last_name="Arora", middle_name="No_Name")
