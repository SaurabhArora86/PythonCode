# walrus operator allows assignment within an expression (Introduced in Python 3.8)

# BElow code is incorrect as it only works with an expression
# p := (len("Company"))
# print(p)

if (n := len("Saurabh")) > 5:  # here we have used walrus operator to assign length of name to n and then check if it is greater than 5
    print(f"Length of name is {n}")
else:
    print(f"Length of name is {n}")


# type assignment operator (Introduced in Python 3.9)

def sum(a: int, b: int) -> int:  # Here we have explictely specificed a, b and return type as int
    return a + b


print(sum(3, 5))


# Match status operator introduced in Python 3.10

def http_status(n):
    match n:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:  # this is default if no other condition is true
            print("Unknown Error")


http_status(404)


def letter(abc):
    match abc:
        case 'Saurabh':
            print("You are correct")
        case 'Daurabh':
            print("You are wrong")
        case _:
            print("Youa re always incorrect")


letter("Saurabh")

# dictionary merged introduced in Python 3.9, its syntax is d1 | d2 where d1 is first dictionary and d2 is second dictionary

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = d1 | d2
print(merged)
