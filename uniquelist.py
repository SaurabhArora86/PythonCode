number = [1, 2, 2, 3, 4, 4, 5, 6]

unique = []

for item in number:
    if item not in unique:
        unique.append(item)

print(unique)

set_value = set(number)

print(list(set_value))

# Another example

values = ["apple", "orange", "apple", "banana"]

uniq = []

for item in values:
    if item not in uniq:
        uniq.append(item)

print(uniq)
