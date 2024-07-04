import random


def x(a, b): return a*b


print(x(10, 20))

# x = lambda a : random.randint(2,10)* a


def x(a): return random.randint(2, 10) * a


print(x(10))
