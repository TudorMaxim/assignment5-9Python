'''
Created on Nov 5, 2017

@author: Tudor
'''

class Student:
    def __init__(self, studentID, name, group):
        self._studentID = studentID
        self._name = name
        self._group = group
    
    def __equ__(self, other):
        return self._studentID == other.get_ID()
    
    def __lt__(self, other):
        return self._studentID < other.get_ID()
    
    def __gt__(self, other):
        return self._studentID > other.get_ID()
        
    def get_ID(self):
        return self._studentID
        
    def get_name(self):
        return self._name
    
    def get_group(self):
        return self._group
    
    def set_ID(self, studentID):
        self._studentID = studentID
        return self._studentID
    
    def set_name(self, name):
        self._name = name
        return self._name
        
    def set_group(self, group):
        self._group = group
        return self._group
    
class Assignment:
    def __init__(self, assignmentID, description, deadline):
        self._assignmentID = assignmentID
        self._description = description
        self._deadline = deadline
    
    def __equ__(self, other):
        return self._assignmentID == other.get_ID()
    
    def __lt__(self, other):
        return self._assignmentID < other.get_ID()
    
    def __gt__(self, other):
        return self._assignmentID > other.get_ID()   
     
    def get_ID(self):
        return self._assignmentID
    
    def get_description(self):
        return self._description
    
    def get_deadline(self):
        return self._deadline
    
    def set_ID(self, assignmentID):
        self._assignmentID = assignmentID
        return self._assignmentID
    
    def set_description(self, description):
        self._description = description
        return self._description
        
    def set_deadline(self, deadline):
        self._deadline = deadline
        return self._deadline
    
class Grade:
    def __init__(self, assignmentID, studentID, grade):
        self._ID = int(str(studentID) + str(assignmentID))
        self._assignmentID = assignmentID
        self._studentID = studentID
        self._grade = grade
    
    def __equ__(self, other):
        return self._ID == other.get_ID()
    
    def __lt__(self, other):
        return self._ID < other.get_ID()
    
    def __gt__(self, other):
        return self._ID > other.get_ID()    
       
    def get_ID(self):
        return self._ID
        
    def get_studentID(self):
        return self._studentID
    
    def get_assignmentID(self):
        return self._assignmentID
    
    def get_grade(self):
        return self._grade
    
    def set_studentID(self, studentID):
        self._studentID = studentID
        return self._studentID
        
    def set_assignmentID(self, assignmentID):
        self._assignmentID = assignmentID
        return self._assignmentID
    
    def set_grade(self, grade):
        self._grade = grade
        return self._grade
    
    
    
