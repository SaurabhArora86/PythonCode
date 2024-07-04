try:
    age = int(input("Enter Age "))
    print(age)
    income = 22000
    risk = income/age
# this is the error type for mismatch in datatypes
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age cannot be zero")


try:
    print(x)
except NameError:
    print("X is not available")
except:
    print("X is not defined")
