import EventModel
class ControllerEvent():

    def __init__(self):
        self.__events = {}

    def addEvent(self, name, date, location, province, registrPrice):
        if(self.__events.get(name) == None):
            event = EventModel.EventModel(name, date, location, province, registrPrice)
            self.__events[name] = event
            return True
        
        return False