import InvoiceModel
class InvoiceController():
    
    def __init__(self):
        self.__invoices = {}
    
    def addInvoice(self, id , date, nif, vat, lines):
        if (self.__invoices.get(id) == None):
            invoice = InvoiceModel.InvoiceModel(id, date, nif,vat)
            invoice.setInvoiceLines(lines)
            self.__invoices[id] = invoice
            return True

        return False

    def listInvoices(self, isPaid):
        list = []
        for id, invoice in self.__invoices.items():
            if invoice.getPaid() == isPaid:
                list.append(invoice)
        return list