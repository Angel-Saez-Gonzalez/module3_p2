class stackLifo():
    
    def __init__(self):
        self.__mystack = []

    def push(self, elem):
        self.__mystack.append(elem)

    def pop(self):
        if len(self.__mystack) > 0:
            return self.__mystack.pop()
        return None

stack = stackLifo()
stack.push(5)
stack.push(6)

print(stack.__dict__)
print(stack._stackLifo__mystack)