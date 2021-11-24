import InvoiceController
from datetime import datetime
import matplotlib.pyplot as plt

def readID():
    while True:
        id = int(input("Input a ID: "))
        if id > 0:
            return id
        else:
            print("Invalid ID")
        
def readDate():
    while True:
        date = str(input("Put the date ex:02/05/2001"))
        if(date.datetime.strptime(date, '%d/%m/%y')):
            formatDate = date.strftime("%d/%m/%Y")
            return formatDate
            break
        else:
            return print("Format error")

def readNIF():
    

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

def readVAT():
    while True:
        vat = float(input("VAT: "))
        if vat > 0:
            return vat
        else:
            print("Error vat null")
            False

ctrl = InvoiceController.InvoiceController

while True:
    print("Invoice  Managment----------------------------")
    print("1.- Add Invoice")
    print("2.- List not paid invoices by custumer NIF")
    print("3.- List paid invoices by custumer NIF")
    print("4.- Pay Invoice")
    print("5.- Exit")

    print("Choose option:")
    option = int(input())

    if option == 1:
        id = readID()
        date = readDate()
        nif = readNIF()
        
        print("Add the lines of the invoice: ")
        lines = []
        while True:
            #product = readProduct()
            #quantity = #readQuantity()
            #totalpro = #readTotalPro()
            lines.append((product, quantity, totalpro))
            optionLines = int(input("To add line ---> 1 / to stop ---> 0: "))
            if optionLines == 0:
                break
        if ctrl.addInvoice(id, date, nif, 0,21, lines):
            print("Created")
        else:
            print("Error")
        
    if option == 2:
        listInv = ctrl.listInvoices(False)
        invoicesID = []
        invoicesTotal = []
        for invoice in listInv:
            print(invoice.getID())
            print(invoice.getDate())
            print(invoice.getTotal())
            print(invoice.getInvoiceLines())
            invoicesID.append(invoice.getID())
            invoicesTotal.append(invoice.getTotal())
        plt.bar(x = invoicesID, height = invoicesTotal)
        plt.xlabel("ID")
        plt.ylabel("€")
        plt.show()
    
    if option == 3:
        A
    
    if option == 4:
        A
    
    if option == 5:
        break
    