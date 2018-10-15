'''
Created on Dec 11, 2017

@author: Tudor
'''
from repository.repository import Repository
from domain.entities import Grade

class GradeCSVRepository(Repository):
    def __init__(self, fileName = "grades.txt"):
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
                grade = Grade(int(attrs[0]), int(attrs[1]), int(attrs[2]))
                Repository.add(self, grade)
                line = f.readline().strip()
        except IOError:
            return "Error saving file"
        finally:
            f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        grades = Repository.get_all(self)
        for g in grades:
            line = str(g.get_assignmentID()) + "," + str(g.get_studentID()) + "," + str(g.get_grade()) + "\n";
            f.write(line)
        f.close()
        
        
        