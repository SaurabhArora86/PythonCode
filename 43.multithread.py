'''
Multithreading is enabled with class threading
thread.start is used to start a thread and thread.join to wait for thread to finish
'''

import threading
import time


def func(sec):
    print(f"Waiting for {sec} seconds")
    time.sleep(sec)


# func(4)
# func(2)
# Above are executing in sequence, to impart parallelism use below

time1 = time.perf_counter()

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])

t1.start()

t2.start()

# time2 = time.perf_counter()
# print(time2 - time1)

# Below is used to wait for thread to finish
# Uncomment above time2 = time.perf_counter() and comment below code and see the difference


t1.join()
t2.join()
time3 = time.perf_counter()
print(time3 - time1)

# Another example

print("***ANother example***")


def print_num():
    for i in range(1, 6):
        print(i)
        time.sleep(1)


def print_let():
    for i in "ABCDE":
        print(i)
        time.sleep(1.5)


t3 = threading.Thread(target=print_num)
t4 = threading.Thread(target=print_let)

t3.start()
t4.start()

t3.join()
t4.join()
