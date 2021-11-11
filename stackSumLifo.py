import stackLifo

class stackSumLifo(stackLifo.stackLifo):

    def __init__(self):
        super().__init__()
        self.__sum = 0
    
    def getSum(self):
        return self.__sum

    def push(self, elem):
        super().push(elem)
        self.__sum += elem

    def pop(self):
        elem = super().pop()
        if elem != None:
            self.__sum -= elem
        return elem


objsum = stackSumLifo()

objsum.push(7)
print(objsum.getSum)

objsum.push(5)
print(objsum.getSum)

objsum.push(2)
print(objsum.getSum)

objsum.pop()
objsum.pop()
objsum.pop()

objsum.pop()
