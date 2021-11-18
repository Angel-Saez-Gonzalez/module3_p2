import Student, ControllerStudent
import re

def menu():
    print("STUDENT CRUD----------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    print("Choose option:")

def readDNI():
    

    while True:

        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        nif = input("DNI: ")
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dni = nif[:8]
            if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
                if tabla[int(dni)%23] == letraControl:
                    return dni
        else:
            print("Error Validation")

def readName():
    while True:
        name = input("Name: ")
        if len(name) > 0:
            return name
        else:
            print("Error nombre null")
            False
            
    
def readSurname():
    while True:
        surname = input("Surname: ")
        if len(surname) > 0:
            return surname
        else:
            print("Error surname null")
            False
            

def readAge():
    while True:
        age = int(input("Age: "))
        if age > 0:
            return age
        else:
            print("Error Age null")
            False
            
    
def readCity():
    while True:
        city = input("City: ")
        if len(city) > 0:
            return city
        else:
            print("Error city null")
            False
            

def readProvince():
    while True:
        province = input("Province: ")
        if len(province) > 0:
            return province
        else:
            print("Error province null")
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

ctrl = ControllerStudent.ControllerStudent
while True:

    menu()
    option = int(input("option: "))
    if option == 1:
        dni = readDNI()
        name = readName()
        surnames = readSurname()
        age = readAge()
        city = readCity()
        province = readProvince()
        email = readEmail()
        ctrl.addStudent(dni, name, surnames, age, city, province, email)

    if option == 2:
        dni = readDNI()
        if ctrl.delStudent(dni) == True:
            print("Delete succes")
        else:
            print("Failed delete")
    
    if option == 3:
        dni = readDNI()
        
        print("1.- Modify Name")
        print("2.- Modify Surnames")
        print("3.- Modify Age")
        print("4.- Modify City")
        print("5.- Modify Province")
        print("6.- Modify Email")
        print("7.- Exit")

        option = int(input("option: "))
        if option == 1:
            newName = readName()
            prop = {"Name":newName}    
            ctrl.modStudent(dni,prop)
    
    if option == 4:
        dni = readDNI()
        print(ctrl)

    if option == 5:
        print("Chao")
        break







