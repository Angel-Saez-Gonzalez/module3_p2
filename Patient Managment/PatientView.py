import re
import PatientController

class PatientView():

    def menu():
        print("Iabi Clinics----------------------------")
        print("1.- Add Patient")
        print("2.- Delete Patient")
        print("3.- Get Patient History")
        print("4.- List patients")
        print("5.- Add appointment")
        print("0.- Exit")

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

    def readName():
        while True:
            name = input("Name: ")
            if len(name) > 0:
                return name
            else:
                print("Error nombre null")
                False

    def readSurName():
        while True:
            name = input("Surname: ")
            if len(name) > 0:
                return name
            else:
                print("Error Surname null")
                False

    def readYear():
        while True:
            age = int(input("Year: "))
            if age > 0 and len(str(age)) > 3 and len(str(age)) < 5:
                return age
            else:
                print("Year format not valid")
                False

    def readTelephone():
        while True:
            telephone = input("Telephone: ")
            if len(telephone) > 0:
                return telephone
            else:
                print("Error telephone null")
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

    ctrl = PatientController.PatientController()
    while True:
        menu()
        option = int(input("Input an option: "))

        if option == 1:
            dni = readDNI()
            name = readName()
            surname = readSurName()
            year = readYear()
            telephone = readTelephone()
            email = readEmail()

            if(ctrl.addPatient(dni, name, surname, year, telephone, email)):
                print("Created!!")
            else:
                print("Failed to create")

        if option == 2:
            dni = readDNI()
            if(ctrl.deletePatient(dni)):
                print("Patient with DNI:", dni,"has been succesfully deleted!!")
            else:
                print("The patient hasn't been deleted")

        if option == 3:
            dni = readDNI()
            compr = ctrl.getPatientHistory(dni)
            if(compr == False):
                print("The patient hasn't had any hitory yet")
            else:
                print(compr)

        if option == 4:
            print("List of patients")
            print("-------------------------")
            patients = ctrl.getPatients()
            for a, values in patients.items():
                print("-------------------------")
                print("Patient with DNI: ",a)
                print(values)
                
        if option == 5:
            dni = readDNI()
            visit = input("Input the visit")
            if(ctrl.addAppointment(dni,visit)):
                print("Appointment created!!!")
            else:
                print("Error to create an appointment") 
    
        if option == 0:
            print("Succesfully exit!!")
            break