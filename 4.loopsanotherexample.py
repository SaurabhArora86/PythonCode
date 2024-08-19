colors = ["Red", "Yellow", "Green"]
for color in colors:
    if color == "Yellow":
        for val in color:
            print(val, end=", ")
    else:
        print("\n", color)

count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("Over with while loop")
