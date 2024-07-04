'''
List - allow duplicates, ordered and addition, removal and change possible
[]
Tupple - immutable (no change allowed, cannot add or delete), ordered and duplicates allowed
    immutable and ordered
()
Set - unique values but addition and removal allowed, no duplicates and ordered
    unique and unordered
{}
Dictionary - Key, value pair
{}
'''

# list to set

my_list = [1, 2, 4, 3, 5, 1, 2, 3, 45]

my_set = set(my_list)
print(my_set)

set1 = {1, 2, 3, 4, 5}
for item in set1:
    print(item)
set1.add(10)
print(set1)
set1.remove(10)
print(set1)

# pop removes the first element
set1.pop()
print(set1)
