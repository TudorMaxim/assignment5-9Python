'''
Created on Nov 6, 2017

@author: Tudor
'''

class Students:
    def __init__(self, repository):
        self.__repository = repository
     
    def get_students(self):
        return self.__repository.get_all()
    
    def get_student(self, key):
        return self.__repository.get_item(key) 
       
    def add_student(self, student):
        return self.__repository.add(student)
    
            
    def remove_student(self, student):
        self.__repository.delete(student.get_ID())
        
    def update_student(self, student, new_student):
        
        if student.get_ID() == new_student.get_ID():
            self.__repository.update(new_student)
        else :
            self.__repository.delete(student.get_ID())
            self.__repository.add(new_student)


    def exist_student(self, studentID):
        return self.__repository.find_by_id(studentID)
        
    def exist_group(self, group):
        for student in self.__students:
            if student.get_group() == group:
                return True
        return False