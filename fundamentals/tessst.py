class Underscore:
    def filter(self, iterable, callback):
        newList = []
        for i in iterable:
            if callback(i):
                newList.append(i)
        return newList    
    def map(self, iterable, callback):
        newList = []
        for i in iterable:
            newList.append(callback(i))
        return newList
    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i
    def reject(self, iterable, callback):
        for i in iterable:
            if callback(i):
                iterable.remove(i)
        return iterable

_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

multiplicados = _.map([1,2,3], lambda x: x*2)

encontrado = _.find([1,2,3,4,5,6], lambda x: x>4)

excluidos = _.reject([1,2,3,4,5,6], lambda x: x%2==0)


