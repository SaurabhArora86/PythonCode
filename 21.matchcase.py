x = int(input("Enter Value for x: "))

match x:
    case 0:
        print("Input value is zero")
    case 4:
        print("Value is 4")
    # Default case
    case _:
        print("Input value is ", x)


###

y = int(input("Enter Value for y: "))

match y:
    case 0:
        print("Input value is zero")
    case 4:
        print("Value is 4")
    # Default case
    case _ if y < 10:
        print("Input value is ", y)

    case _:
        print("Input value is greater than 10 and value is ", y)
