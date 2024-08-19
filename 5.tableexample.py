
y = int(input("Enter Number fot table"))

for i in range(1, 12):
    if i == 11:
        break
    print(y, "X", i, "=", y*i)
