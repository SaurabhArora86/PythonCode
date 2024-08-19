# Custom Errors are raised with raise keyword
# Useful when u want to validate the integrity of data before program moves forward and crashes later on

a = int(input("Enter number between 5 and 9"))

if (a < 5 or a > 9):
    raise ValueError("Number not between 5 and 9")
