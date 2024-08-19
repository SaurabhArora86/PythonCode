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

# pop removes the first element from set but the catch is set is unordered so it becomes random
set1.pop()
print(set1)

# Empty sets are created with set()
# because if you do a = {}, this will create an empty dictionary
# Reason: Sets and Dictionary have same curly braces

p = set()
print(type(p))


# set methods


# union and update
# union and update both updates the set with value of 2nd set but union returns a new set where as update, updates an existing set

s1 = {2, 3, 4, 5, 3}
s2 = {2, 7, 8, 9}
print(s1, s2, s1.union(s2))
print(s1.update(s2))
print(s1)

# Intersection and Intersection update is same in terms of updating an existing set or new set
s1 = {2, 3, 4, 5, 3}
s2 = {2, 7, 8, 9}
print(s1, s2, s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1)

# difference and difference_update is same in terms of updating an existing set or new set
# difference gives value present in first set but not in second set
s1 = {2, 3, 4, 5, 3}
s2 = {2, 7, 8, 9}
print(s1, s2, s1.difference(s2))
print(s1.difference_update(s2))
print(s1)

# remove()/discard() is used to remove values from set
# difference is - remove will raise an error if the value is not present where as discard wont raise an error
s1 = {2, 3, 4, 5, 3}
s1.remove(3)
print(s1)
s1.discard(9)
print(s1)


# del is a keyword not a method to delete a set del <setname>
# to empty a set use clear()
s1.clear()
print(s1)
