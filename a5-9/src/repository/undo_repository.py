'''
Created on Nov 28, 2017

@author: Tudor
'''
from MyVector.MyVector import MyVector

class UndoRepository():
    def __init__(self):
        self.__repository = MyVector([])
    
    def get_last(self):
        l = len(self.__repository)
        if l == 0:
            return 0
        return self.__repository[l - 1]
    
    def add(self, obj):
        self.__repository.push_back(obj)
        
    def pop(self):
        l = len(self.__repository)
        self.__repository.__delItem__(l - 1)