class Student():

    def __init__(self, dni, name, surnames, age, city, province, email):
        self.__dni = dni
        self.__name = name
        self.__surnames = surnames
        self.__age = age
        self.__city = city
        self.__province = province
        self.__email = email
    
    def getDNI(self):
        return self.__dni

    def setDNI(self, dni):
        self.__dni = dni

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSurnames(self):
        return self.__surnames

    def setSurnames(self, surnames):
        self.__surnames = surnames

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getCity(self):
        return self.__city

    def setCity(self, city):
        self.__city = city

    def getProvince(self):
        return self.__province

    def setProvince(self, province):
        self.__province = province

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email
