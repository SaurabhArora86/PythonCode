price = 10

if price < 5:
    print("Price is cheap")
    print("can afford")
elif price > 2:
    print("Under first elif")
elif price > 5:
    print("Not that pricey - under second elif")
elif price < 11:
    print("Not that pricey - under third elif")

else:
    print("NON pricey")


# Another example with SyntaxWarning

value = "My weight"

if ("y" in value):
    print("Y found")
elif ("w" in value):
    print("W found")
else:
    print("Nothing found")

# ANother example

weight = input("Enter Weight ")

measurement = input("(K)g or (L)bs ")

if measurement == "K" or measurement == 'k':
    print("Your weight is " + weight, measurement)
elif measurement == "L" or measurement == 'l':
    print("Your weight is " + weight, measurement)

a = int(input("Enter your age: "))

if a == 0:
    print(f'Entered age is {a} which is not valid')
elif (a < 0):
    print(f'Entered age is  {a} which is not valid again')
elif (a > 45):
    if (a > 60):
        print(f'Entered age is {a} which is a valid age but you are old')
    else:
        print(f'Entered age is {a} which is not that old')
else:
    print("You are Young")


# while

i = 1
while i <= 3:
    print("Value is " + str(i))
    i = i+1

print(i)

i = 1
while i <= 3:
    y = i
    print(i * '*')
    i = i+1
    print((y) * '*')
    y = i

value = "My weight is y"
print(value.split())
if "My" in value.split():
    print("Yes")
else:
    print("My not found")
# while "y" in value.split():
#     print("y")
#     y = y+1


# Another example

budget = 220
apple_price = 210

if (budget < apple_price):
    print("Not able to Buy")
elif (budget == apple_price):
    print("Budget would be lost")
else:
    print("Buying apples")
