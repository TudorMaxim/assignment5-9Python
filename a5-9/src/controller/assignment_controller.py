'''
Created on Nov 6, 2017

@author: Tudor
'''

class Assignments:
    def __init__(self, repository):
        self.__repository = repository
     
    def get_assignments(self):
        return self.__repository.get_all()
    
    def get_assignment(self, key):
        return self.__repository.get_item(key)
        
    def add_assignment(self, assignment):
        return self.__repository.add(assignment)
    
    def list_assignments(self):
        return self.__repository.get_all()
            
    def remove_assignment(self, assignment):
        self.__repository.delete(assignment.get_ID())
    
    def update_assignment(self, assignment, new_assignment):
        if assignment.get_ID() == new_assignment.get_ID():
            self.__repository.update(new_assignment)
        else :
            self.__repository.delete(assignment.get_ID())
            self.__repository.add(new_assignment)
    
    def exist_assignment(self, assignmentID):
        return self.__repository.find_by_id(assignmentID)
    
    