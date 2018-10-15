'''
Created on Dec 11, 2017

@author: Tudor

'''
from repository.repository import Repository
from domain.entities import Student

class StudentCSVRepository(Repository):
    def __init__(self, fileName = "students.txt"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, client):
        Repository.add(self, client)
        self.__storeToFile()
    
    def delete(self, clientId):
        Repository.delete(self, clientId)
        self.__storeToFile()        
    
    def update(self, newClient):
        Repository.update(self, newClient)
        self.__storeToFile()
    
    def __loadFromFile(self):
        f = open(self.__fName, "r")
        try:
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                student = Student(int(attrs[0]), attrs[1], int(attrs[2]))
                Repository.add(self, student)
                line = f.readline().strip()
        except IOError:
            return "Error saving file"
        finally:
            f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        students = Repository.get_all(self)
        for s in students:
            line = str(s.get_ID()) + "," + s.get_name() + "," + str(s.get_group()) + "\n";
            f.write(line)
        f.close()
