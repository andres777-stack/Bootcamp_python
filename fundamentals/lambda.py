class Underscore:
    def map(self, iterable, callback):
        # tu código aqui
    def find(self, iterable, callback):
        # tu código aqui
    def filter(self, iterable, callback):
        newList = []
        for i in iterable:
            if callback(i):
                newList.append(i)

    def reject(self, iterable, callback):
        # tu código 
# has creado una libreria con 4 métodos
# se crea la instancia de la clse
_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba

_.map([1,2,3], lambda x: x*2) # debe retornar [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # debe retornar el primer valor que es mayor que 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debe retornar [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # debe retornar [1,3,5]

