'''
Created on Dec 11, 2017

@author: Tudor
'''
from repository.repository import Repository
from domain.entities import Assignment

class AssignmentCSVRepository(Repository):
    def __init__(self, fileName = "assignments.txt"):
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
                assignment = Assignment(int(attrs[0]), attrs[1], attrs[2])
                Repository.add(self, assignment)
                line = f.readline().strip()
        except IOError:
            return "Error saving file"
        finally:
            f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        assignments = Repository.get_all(self)
        for a in assignments:
            line = str(a.get_ID()) + "," + a.get_description() + "," + a.get_deadline() + "\n";
            f.write(line)
        f.close()
