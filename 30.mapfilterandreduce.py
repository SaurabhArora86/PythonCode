# map allows taking in multiple inputs and applies a function to that input
# for eg: what if you want to pass a list to a cube function
# without map example below:

from functools import reduce
l = [1, 2, 3, 4, 5, 6]


def cube(x):
    return (x*x*x)


l1 = []

for item in l:
    l1.append(cube(item))

print(l1)


# With map

l2 = list(map(cube, l))
print(l2)

# Filter is used to filter out values from input
# Note Map, reduce and filter are called higher order fucntion as they take function as argument


def value_greater(x):
    return x > 4


l3 = list(filter(value_greater, l))
print(l3)


# Reduce is used for iterating over iterable like map or filter but it reduces the overall value

def sum(x, y):
    return (x+y)


l4 = reduce(sum, l)
print(l4)
