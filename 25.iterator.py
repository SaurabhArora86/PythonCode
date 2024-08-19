# List, Tuple, Strings all are iterable Object on which iterator function can act
name = ["john", "cena", "hulk", "batman", "spiderman"]

my_iter = iter(name)
for item in my_iter:
    print(item)

# ANother way is using next(), note: for loop creators an iterator object and executes next() method

my_iter = iter(name)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
