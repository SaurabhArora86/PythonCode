'''
Generators are used to generate values on fly using yield statement
Advantage over list, tupes, sets: They dont store value and generates value when requested
This saves memory
'''


def my_generator():
    for i in range(6):
        yield i


my_gen = my_generator()
print(next(my_gen))
print(next(my_gen))
print("Hello")

for j in my_gen:
    print(j)
