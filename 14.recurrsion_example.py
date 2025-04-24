'''
factorial(4) = 4*3*2*1
factorial(0) or factorial(1) is 1
'''


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorial(n-1))


print(factorial(4))


def factor(n):
    if n == 1:
        return 1
    else:
        y = n * factor(n-1)
    return (y)


print(factor(5))
