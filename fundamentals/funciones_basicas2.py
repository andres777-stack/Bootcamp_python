def myFuncion(num):
    cuentaRegresiva = []
    for i in range(num, 0, -1):
        cuentaRegresiva.append(i)
    return cuentaRegresiva

print(myFuncion(10))

def myFunction(list):
    print(list[0])
    return list[1]

myFunction([3, 4])

def myFunction(list):
    return list[0] + len(list)

print(myFunction([3, 4]))

def myFunction(list):
    newList = []
    counter = 0
    for i in list:
        if i > list[1]:
            newList.append(i)
            counter += 1
    if len(newList) < 2:
        return False
    print(counter)
    return newList


var = myFunction([1, 2, 3])
print(var)

def myFunc(size, value):
    newList = []
    for i in range(0, size):
        newList.append(value)
    return newList

var = myFunc(5, 2)
print(var)
