import datetime
import ControllerEvent
import re
    
def menu():
    print("Event  Managment----------------------------")
    print("1.- Add Event")
    print("2.- dd participant to an Event")
    print("3.- List pending events with participants")
    print("4.- List Event finished with podium")
    print("5.- Finish an Event")
    print("0.- Exit")

def readName():
    while True:
        name = input("Name: ")
        if len(name) > 0:
            return name
        else:
            print("Error nombre null")
            False

def readDate():
    while True:
        strdate = str(input("Put the date ex:02/05/2001: "))
        obj = datetime.strptime(strdate, '%d/%m/%y')
        formatDate = datetime.strftime(obj, "%b %d/%Y")
        return formatDate
        

def readLocation():
    while True:
        name = input("Location: ")
        if len(name) > 0:
            return name
        else:
            print("Error Location null")
            False

def readProvince():
    while True:
        name = input("Province: ")
        if len(name) > 0:
            return name
        else:
            print("Error Province null")
            False

def readRegistrationPrice():
    while True:
        price = float(input("Input a price: "))
        if price > 0:
            return price
        else:
            print("Invalid price")

def readDNI():
    while True:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        nif = input("NIF: ")
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dni = nif[:8]
            if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
                if tabla[int(dni)%23] == letraControl:
                    return dni
        else:
            print("Error Validation")

def readAge():
    while True:
        age = int(input("Age: "))
        if age > 0:
            return age
        else:
            print("Error Age null")
            False

def readEmail():
    while True:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = str(input("Email: "))
        if(re.fullmatch(regex, email)):
            return email
        else:
            print("Invalid Email")
            False


ctrl = ControllerEvent.ControllerEvent
while True:
    menu()
    option = int(input("Choose an option: "))

    if option == 1:
        name = readName()
        date = readDate()
        location = readLocation()
        province = readProvince()
        price = readRegistrationPrice()

        if(ctrl.addEvent(name, date, location, province, price)):
            print("Created event")
        else:
            print("Failed to create")

    if option == 2:
        pass

    if option == 3:
        pass

    if option == 4:
        pass

    if option == 5:
        pass

    if option == 0:
        break