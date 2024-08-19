name = "Mango"


#print(names[0:-1])
# Starts with 0 index and gies till n-1 for [0:n] and prints it
# -1 is the last character, -3 becomes third last

print(name[:4]) # Same as print(name[0:4])
print(name[:])
print(name[:-1])
print(name[1:-1])
# Below will just print last char, reason: it goes from first: last which is -1 so it becomes -1:-1
print(name[-1:])
print(name[0:])
