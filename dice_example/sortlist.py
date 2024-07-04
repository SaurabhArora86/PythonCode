list1 = [1, 2, 4, 2, 5, 6, 3]

for i in range(0, len(list1)):
    for y in range(i+1, len(list1)):
        if list1[i] > list1[y]:
            list1[i], list1[y] = list1[y], list1[i]

print(list1)


list2 = [1, 2, 3]
list2.sort(reverse=True)
print(list2)
