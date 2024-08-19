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

val = "S"

# Below exception method is a standard template used to prevent python from breaking up
try:
    for i in val:
        print(int(i))
except Exception as e:
    print(e)
print("End of try")

# finally:
# This has usage inside functions
# Whether try works or except works, finally will always get executed along


def func1():
    try:
        a = [1, 2, 3, 4]
        b = int(input("Enter value of b: "))
        for val in a:
            if b == val:
                return b
                break
    except:
        return 0
    finally:
        print("I am always executed")


x = func1()
print(x)
