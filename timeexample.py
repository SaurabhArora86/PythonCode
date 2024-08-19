import time
# import datetime

# # print(time.strftime())

# a = datetime.datetime.now()
# print(a)
current_time = time.strftime("%H:%M:%S")
print(current_time)

list1 = current_time.split(":")
print(list1[0])
if (int(list1[0]) > 12):
    print("Its afternoon")
elif (int(list1[0]) == 12):
    print("Its Noon")
else:
    print("Its Morning")
