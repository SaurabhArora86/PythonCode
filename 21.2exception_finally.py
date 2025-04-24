'''
Finally runs no matter what. It is used to clean up resources.

Note: If u are running finally without function, it is as similar as running simple print statement
But in case finally is run with function with return, it will run the function and then run finally block even in case of return
'''

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
except:
    print("Invalid input")
finally:
    print("I am always executed")
print("Hello, prgrarm is still running")

# Above has no actual use of finally where as when used in function, it has a use


def main():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter second number: "))

        return a/b
    except:
        return ("Invalid input")

    finally:
        print("I am always executed")
    print("Hello, prgrarm is still running")
# Above print will not run since hte function has return but finally will run


main()
