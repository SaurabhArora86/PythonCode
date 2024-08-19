name = ["john", "cena", "hulk", "batman", "spiderman"]
print(name[0])
print(name[-1])
print(name[:2])
print(name[2:])
print(name[0:2])
name[0] = "jon"
print(name)

# list methods

number = [1, 2, 3, 4, 5, 6, 7]
print(number)

number.append(8)
print(number)

number.insert(0, -1)
print(number)

number.remove(3)
print(number)

print(1 in number)
print(len(number))

number.clear()
print(number)

# 2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][2])
for row in matrix:
    for item in row:
        print(item)


# List comprehension

list1 = [i*i for i in range(4)]
print(list1)
