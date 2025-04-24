# Sum of natural numbers is sum of number to its lesser numbers
# eg: 4 = 4+3+2+1 = 10

num = int(input("Enter a number: "))

sum = 0
for i in range(1, num+1):
    sum = sum + i
print(f"Sum of natural numbers is {sum}")
