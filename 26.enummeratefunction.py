# Enumerate function gives index and value as a tuple
# You can unpack tupple with a for loop

list1 = [10, 20, 30, 40, 10]

for index, val in enumerate(list1):
    if (index == 2):
        print("Value is ", val)

for i in enumerate(list1):
    print(i)
