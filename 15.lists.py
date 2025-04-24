# List can store values of different types
# List is mutable
# List can be accessed using index
# List can be sliced
# List can be iterated
# List can be nested
# List can be extended
# List can be appended
# List can be inserted
# List can be removed
# List can be cleared
# List can be checked for value
# List can be sorted

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

print(number.sort())  # sorts in ascending order
# Note above will return NONE as it sorts the number but does not return anything
print(number.reverse())  # sorts in descending order
# Note above will return NONE as it reverses the number but does not return anything
number.index(5)  # returns index of 5

print(number)
# number.clear()
# Adding two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

# 2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][2])
for row in matrix:
    for item in row:
        print(item)

list1 = ["Ram", "Shyam", "Hari"]
a = input("Enter a name: ")

if (a in list):
    print("Name found")

# List comprehension

list1 = [i*i for i in range(4)]
print(list1)


list4 = [1, 2, 3, 4]

list_squared = [i*i for i in list4]
print(list_squared)
