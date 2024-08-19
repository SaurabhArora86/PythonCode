# f = open("myfile.txt", 'w')
# f.write("THis is referenced file for 28.fileio.py")
# f.close()


# f = open("myfile.txt", 'r')
# text = f.read()
# print(text)

# Above can be accomplished as below but we dont need to use f.close()

with open("myfile.txt", "r") as f:
    print(f.read())

with open("myfile.txt", 'a') as f:
    f.write("\nAwesome!!!")

with open("myfile.txt", 'r') as f:
    print(f.read())
