list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
result = []

for i in list1:
    for n in list2:
        result.append(i * n)

print(result)