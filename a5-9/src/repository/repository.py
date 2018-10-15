'''
Created on Nov 19, 2017

@author: Tudor
'''
from MyVector.MyVector import MyVector

class Repository(object):
    
    def __init__(self):
        self.__items = MyVector([])
        
    def add(self, item):
        val = self.find_by_id(item.get_ID())
        if val != 0:
            return 1
        self.__items.push_back(item)
        return 0
        
    def delete(self, Id):
        item = self.find_by_id(Id)
        self.__items.pop(item)
             
    def update(self, item):
        for i in range(0, len(self.__items)):
            if self.__items[i].get_ID() == item.get_ID():
                self.__items.__setItem__(i, item)
        
    def make_zero(self, ID):
        for i in range (0, len(self.__items)):
            if self.__items[i].get_ID == ID:
                self.__items[i].set_grade(0)
                
    def size(self):
        return len(self.__items)
    
    def assign(self, key, item):
        for i in range(0, len(self.__items)):
            if self.__items[i].get_ID() == key:
                self.__items[i].set_grade(item.get_grade())
        
    def get_all(self):
        return self.__items
    
 
    def get_item(self, key):
        for i in range(0, len(self.__items)):
            if self.__items[i].get_ID() == key:
                return self.__items[i]
        return 0
    
    def find_by_id(self, Id):
        for i in range(0, len(self.__items)):
            if self.__items[i].get_ID() == Id:
                return self.__items[i]
        return 0
    
    
    
class OldRepository(object):
    def __init__(self):
        self.__items = {}
        
    def add(self, item):
        val = self.find_by_id(item.get_ID())
        if val != 0:
            return 1
        self.__items[item.get_ID()] = item
        return 0
        
    def delete(self, Id):
        item = self.find_by_id(Id)
        self.__items.pop(item.get_ID())
             
    def update(self, item):
        for i in range(0, len(self.__items)):
            if i == item.get_ID():
                self.__items[i] = item
        
    def make_zero(self, ID):
        self.__items[ID].set_grade(0)
                
    def size(self):
        return len(self.__items)
    
    def get_all(self):
        return list(self.__items.values())
    
    def assign(self, key, item):
        self.__items[key] = item
        
    def get_item(self, key):
        return self.__items[key]
    
    def find_by_id(self, Id):
        if not Id in self.__items:
            return 0
        return self.__items[Id]
    
    
    
