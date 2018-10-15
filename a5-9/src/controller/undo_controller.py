'''
Created on Nov 28, 2017

@author: Tudor
'''
class UndoController():
    def __init__(self, repository):
        self.__operations = repository
    
    def pop(self):
        self.__operations.pop()
        
    def get_last(self):
        return self.__operations.get_last()
    
    def add(self, obj):
        self.__operations.add(obj)