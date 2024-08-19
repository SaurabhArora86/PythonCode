import random


def x(a, b): return a*b


print(x(10, 20))

# x = lambda a : random.randint(2,10)* a
# variable which otherwise is used as function = lambda input:output
# i.e lambda arguments:expression
# for eg:

'''
def doubel(a):
    return a*2

Can be written as

doubel = lambda a:a*2

Similarly avg = lambda x,y:(x+y)/2
'''


def x(a): return random.randint(2, 10) * a


print(x(10))


def avg(x, y): return (x+y)/2


print(avg(2, 3))
