# A number is primt if it is only divided by 1 and number itself

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
