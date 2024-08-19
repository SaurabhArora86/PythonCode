price = 10

print(price < 10)

print(price > 5 and price <= 10)
print(price > 5 or price < 5)
print(not (price > 5))


# Arithmetic operator
# ** becomes power
# // gives int ouput like 10//3 gives 3
# % gives remainder for eg: 5%3 gives 2

'''
is and == both are comparison operators but when you do
a=3
b=3
and ==b or a is b, output will be true
but when you do
a = [1,2,3]
b = [1,2,3]

a is b will come out to be false where as a ==b will come out to be true

Reason:
a is b is true when it refers to same memory location
Python provides same memory location to constants or immutables like tuple when assignment happens more than once
whereas a==b compares values (unlike "is" which compares value at memory location) and works for lists as well which are changable
'''
