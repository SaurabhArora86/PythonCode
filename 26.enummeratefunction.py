# Enumerate function gives index and value as a tuple
# You can unpack tupple with a for loop
# works only with list, tuple, string

list1 = [10, 20, 30, 40, 10]

for index, val in enumerate(list1):
    if (index == 2):
        print("Value is ", val)

for i in enumerate(list1):
    print(i)

# Wont work with dictionary

dict1 = {"name": "John", "age": 25, "city": "New York"}

for key, value in enumerate(dict1):
    print(key, value)
    print(value)
print(dict1.keys())
