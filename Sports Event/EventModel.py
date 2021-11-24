class EventModel():

    def __init__(self, name, date, location, province, registrationPrice):
        self.__name = name
        self.__date = date
        self.__location = location
        self.__province = province
        self.__registrationPrice = registrationPrice
        self.__totalEvent = 1
        self.__listParticipants = []
        self.__finished = False
        self.__podium = {}

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    def getDate(self):
        return self.__date

    def setDate(self, date):
        self.__date = date

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        self.__location = location

    def getProvince(self):
        return self.__province

    def setProvince(self, province):
        self.__province = province

    def getRegistrationPrice(self):
        return self.__registrationPrice

    def setRegistrationPrice(self, registrationPrice):
        self.__registrationPrice = registrationPrice

    def getTotalEvent(self):
        return self.__totalEvent


    def getListParticipants(self):
        return self.__listParticipants

    def setListParticipants(self, listParticipants):
        self.__listParticipants = listParticipants

    def getFinished(self):
        return self.__finished

    def setFinished(self, finished):
        self.__finished = finished

    def getPodium(self):
        return self.__podium
