def myF(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
                i += 1
    for k in range(len(list) - 2, 0, -1):
        for b in range(i + 1, 1, -1):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
                i -= 1
    return list

var = myF([3, 6, 8, 12, 1])

print(var)