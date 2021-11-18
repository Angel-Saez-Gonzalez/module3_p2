class InvoiceModel():
    def __init__(self, id, date, customerNIF, vat):
        self.__id = id
        self.__date = date
        self.__customerNIF = customerNIF
        self.__paid = False
        self.__base = 0
        self.__vat = vat
        self.__total = 1
        self.__invoiceLines = []
    
    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id == id

    def getDate(self):
        return self.__date

    def setDate(self, date):
        self.__date == date

    def getCustomerNIF(self):
        return self.__customerNIF

    def setCustomerNIF(self, customerNIF):
        self.__customerNIF == customerNIF

    def getPaid(self):
        return self.__paid

    def setPaid(self):
        self.__paid = True

    def getBase(self):
        return self.__base

    def setBase(self, base):
        self.__base == base

    def getVAT(self):
        return self.__vat

    def setVAT(self, vat):
        self.__vat == vat

    def getTotal(self):
        return self.__total

    def setTotal(self, total):
        self.__total == total
    
    def getInvoiceLines(self):
        return self.__invoiceLines

    def setInvoiceLines(self, invoiceLines):
        self.__invoiceLines = invoiceLines
        for line in invoiceLines:
            self.__base += line[2]
        self.__total *= self.__base*(1+self.__vat)