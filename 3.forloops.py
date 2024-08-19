number = [1, 2, 3, 4, 5]

for i in number:
    print(i)

# Same code with while
y = 0
while y < len(number):
    print(number[y])
    y = y+1

# range
print("\n")
# range(excluding this number)
# range(start,end(exclusing this number),step)
numbers = range(4, 8, 2)
for item in numbers:
    print(item)

print(range(4))

for i in range(4):
    print(i)

# COnvert list to String
list_val = ["list1", "list2", "list3"]
for i in list_val:
    print(i)
