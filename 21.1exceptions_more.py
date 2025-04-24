
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
except ValueError:
    print("Invalid input")

try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except:
    print("Exception is not explitely handled")

print("Hello, prgrarm is still running")


# In case of raise, program terminates where as in case of exception, exception is caught but program doesnt terminate

if b == 0:
    raise ZeroDivisionError("b cannot be zero")
else:
    print(a/b)


try:
    with open("lists.py", "r") as f:
        f.read()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
