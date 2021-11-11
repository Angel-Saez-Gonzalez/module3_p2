mystack = []

def push(elem):
    mystack.append(elem)

def pop():
    if len(mystack) > 0:
        return mystack.pop()
    return None

def showStack():
    return mystack


while True:
    e = int(input("Option: "))
    if e == 1:
        elem = input("element: ")
        push(elem)
    elif e == 2:
        a = pop()
        if a == None:
            print("Ta vacia chaval")
        else:
            print("The delete element is",a)
    elif e == 3:
        print(showStack())
    elif e == 0:
        break
