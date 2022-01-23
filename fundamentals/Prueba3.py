import random
def myFunction(minValue = 0, maxValue = 100):
    ranNum = random.random() * (maxValue - minValue) + minValue 
    return round(ranNum)

var = myFunction(minValue = 95)
print(var)
