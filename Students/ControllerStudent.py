import Student

class ControllerStudent():

    def __init__(self):
        self.__myStudents={}

    def addStudent(self, dni, name, surnames, age, city, province, email):
        student = Student.Student(dni, name, surnames, age, city, province, email)
        if dni in self.__myStudents.keys():
            return False
        else:
            self.__myStudents[dni] = student
    
    def delStudent(self, dni):
        if dni in self.__myStudents.keys():
            student = self.__myStudents.pop(dni)
            return True
        else:
            return False

    def modStudent(self, dni, properties):
        student = self.__myStudents[dni]
        for prop, value in properties.items():
            if (prop == "Name"):
                student.setName(value)
            if (prop == "Surmame"):
                student.SetSurname(value)