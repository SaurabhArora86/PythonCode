name = "Mango"

# MANGO
# 01234
# -5-4-3-2-1
# print(names[0:-1])
# Starts with 0 index and gies till n-1 for [0:n] and prints it
# -1 is the last character, -3 becomes third last

print(name[:4])  # Same as print(name[0:4])
print(name[:])
print(name[:-1])
print(name[1:-1])
# Below will just print last char, reason: it goes from first: last which is -1 so it becomes -1:-1
print(name[-1:])
print(name[0:])
print(name[0:-1])

print("**********")
print(name[0:-1])  # Mang
print(name[-5:])  # Mango
print(name[1:-4])  # a
print(name[:])  # Mango
print(name[1:])  # ango
print(name[:-1])  # Mang
print(name[1:])  # ango
print(name[:4])  # Mang
print(len(name))  # 5
print(name[-1:])  # o

print("**********")
# skipping values
# print(name[start:stop:step])
print(name[0:5:1])  # Mango
print(name[0::2])  # Mno
print(name[::2])  # Mno

string2 = "01234567"

print(string2[1:6:3])  # 14
print(string2[1:8:3])  # 147

string3 = "abcdefghijlmnopqrstuvwxyz"
#          012345678910111213141516171819
print(string3[1:18:5])  # bgmr
