def myFunction(list):
    for i in range(len(list) - 1):
        minvalue = i
        
        for j in range(i + 1, len(list)):
            if list[j] < list[minvalue]:
                minvalue = j
        
        
        list[minvalue], list[i] = list[i], list[minvalue]
    
    return list
                
        
var = myFunction([4, 5, 7, 1, 2])
print(var)
