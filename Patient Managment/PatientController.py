import PatientModel

class PatientController():

    def __init__(self):
        self.__listPatients = {}

    def addPatient(self, dni, name, surname, birth, tel, email):
        if(self.__listPatients.get(dni) == None):
            patient = PatientModel.PatientModel(dni, name, surname, birth, tel, email)
            self.__listPatients[dni] = patient
            return True
        return False

    def deletePatient(self, dni):
        if(self.__listPatients.get(dni) != None):
            del self.__listPatients[dni]
            return True
        return False

    def getPatientHistory(self, dni):
        if(self.__listPatients.get(dni) != None):
            patient = self.__listPatients[dni]
            historyList = patient.getVisits()
            return historyList
        return None
    
    def getPatients(self):
        return self.__listPatients
