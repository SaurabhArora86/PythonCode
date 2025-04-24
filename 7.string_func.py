cou = "!!!Python for Beginners!!"

print(cou.find("y"))
print(cou.find("z"))

print(cou.replace("for", "4"))


# in operator
print("Python" in cou)

print(cou)

print(cou.split())  # default split is on space
print(cou.split(" "))
print(cou.rstrip("!"))  # removes from right
print(cou.lower())

pou = "python For Beginners!!"

print(pou.capitalize())
print(pou.replace("python", "Golang"))
# replace wont replace the pou value, it will return a new value. Strings are immutable
print(pou)

string1 = "   Hello    "
print(string1.strip())  # removes spaces from both sides
print(string1.lstrip())  # removes spaces from left
print(string1.rstrip())  # removes spaces from right

print(pou.find("F"))  # 7
print(pou.find("f"))  # -1
