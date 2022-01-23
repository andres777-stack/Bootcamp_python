def myF(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

var = myF([4, 2, 8, 3])
print(var)

def funcion():
    x = True
    print("Coding" if x == True else "False")

funcion()
