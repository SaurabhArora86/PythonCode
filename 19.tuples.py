# Tuples are immutable, they cannot be modified

number = (1, 2, 3, 4, 3, 6, 8)

print(number)

print(number.index(3))


values = ("apple", "banana", "orange", "apple")
print(values)
print(values.count("apple"))

if 3 in number:
    print("Tuple has number")

print(number[:4:2])
