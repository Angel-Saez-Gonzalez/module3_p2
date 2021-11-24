class PatientModel():

    def __init__(self, dni, name, surname, birth, tel, email):
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        self.__birth = birth
        self.__tel = tel
        self.__email = email
        self.__visits = []
        self.__numberVisits = 0

    def getDni(self):
       return self.__dni
    
    def setDni(self, dni):
        self.__dni = dni
        
    def getName(self):
       return self.__name
    
    def setName(self, name):
        self.__name = name

    def getSurname(self):
       return self.__surname
    
    def setSurname(self, surname):
        self.__surname = surname

    def getBirth(self):
       return self.__birth
    
    def setBirth(self, birth):
        self.__birth = birth

    def getTel(self):
       return self.__tel
    
    def setTel(self, tel):
        self.__tel = tel

    def getEmail(self):
       return self.__email
    
    def setEmail(self, email):
        self.__email = email

    def getNumberVisits(self):
        return self.__numberVisits

    def getVisits(self):
        return self.__visits

    def setVisits(self, visits):
        self.__visits = visits
        self.__numberVisits += 1    