param = input("What is your age ")
print("Hello your age is " + param)

# Type COnversion

a = input("Enter your birth year ")

age = 2024 - int(a)

print("Age is " + str(age))

# calculator

first = input("Enter first number ")
second = input("Enter second number ")

print("Sum is " + str(int(first) + int(second)))


# multi line string

param1 = input('''
               What is your age
               What is your gender
               What is your pincode
               ''')
print(param1)
