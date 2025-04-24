# In factorial, we have to multiply the number with the previous number until the number is 1.
# for eg: factorial of 5 = 5*4*3*2*1 = 120
# it can be written as factorial(5) = 5*factorial(4)

def factorial(num):
    if (num == 1 or num == 0):
        return 1
    return (num * factorial(num-1))


print(f"Factorial of number is {factorial(5)}")


def sum(num):
    if (num == 0):
        return 0
    return (num + sum(num-1))


print(f"Sum of numbers is {sum(6)}")


def star(m):
    if m == 0:
        return
    print("*" * m)


star(3)


def mul(num):
    for i in range(1, 11):
        print(f" {num} * {i} = {num * i}")


mul(5)
