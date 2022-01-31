class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self
# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!
u = md.add(6).result
print(u)

o = md.add(7).result
print(o)

sust = md.subtract(1, 2, 3, 4).result
print(sust)