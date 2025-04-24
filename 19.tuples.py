# Tuples are immutable, they cannot be modified
# Tuples can have multiple data types
# Tuples can be accessed using index
# Tuples can be sliced
# Tuples can be iterated
# Tuples can be extended
# Tuples can be appended
# Tuples can be cleared

number = (1, 2, 3, 4, 3, 6, 8, "Ram")

print(number)

# Below gives the index of 3
print(number.index(3))


values = ("apple", "banana", "orange", "apple")
print(values)
print(values.count("apple"))

# Below will give error as tuples are immutable
# values[1] = "pineapple"
# But to change convert them to list and then change
values_list = list(values)
values_list[1] = "pineapple"
values = tuple(values_list)
print(values)

if 3 in number:
    print("Tuple has number")

print(number[:4:2])

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

print(tup1 + tup2)
