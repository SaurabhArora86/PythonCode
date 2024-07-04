command = ""
start = False
while True:
    command = input(">").lower()
    if command == "start":
        if start == True:
            print("car is already started")
        else:
            start = True
            print("starting the car....")
    elif command == "stop":
        if not start:
            print("Car is already stopped")
        else:
            start = False
            print("Stopping the car....")
    elif command == 'help':
        print("please enter start, stop or quit")
    elif command == "quit":
        break
    else:
        print("I don't understand the command")
