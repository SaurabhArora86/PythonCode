'''
    *
   ***
  *****
'''

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    # print(, end = " ") will print the space in the same line rather than a new line
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print(" ")  # Here if we print("/n") then it will print the star pattern in new line which becomes 2 lines rather than 1 line gap
