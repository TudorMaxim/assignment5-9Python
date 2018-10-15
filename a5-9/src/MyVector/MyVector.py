'''
Created on Dec 11, 2017

@author: Tudor
'''
from collections.abc import Sequence
from domain.entities import Student

class MyVector(Sequence):
    def __init__(self, l):
        self.__list = l
        self.__index = 0
        super().__init__()  
    
    def __len__(self):
        return len(self.__list)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = self.__list[self.__index]
        except IndexError:
            raise StopIteration()
        self.__index += 1
        return item
    
    def __setItem__(self, index, value):
        self.__list[index] = value
    
    def __delItem__(self, index):
        del self.__list[index]
    
    def push_back(self, item):
        self.__list.append(item)
    
    def pop(self, item):
        index = -1
        for i in range(0, len(self.__list)):
            if self.__list[i] == item:
                index = i
                
        if index > -1:
            del self.__list[index]
                  
    def __getitem__(self, index):
        return self.__list[index]
  
    def swap(self, i, j):
        tmp = self.__list[i]
        self.__list[i] = self.__list[j]
        self.__list[j] = tmp

     
def cmp(x, y):
    if x < y:
        return True
    return False

def make_heap(V, n, i, cmp):
    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2   
    if l < n and cmp(V[i], V[l]):
        largest = l

    if r < n and cmp(V[largest], V[r]):
        largest = r
 
    if largest != i:
        V.swap(i, largest)
        make_heap(V, n, largest, cmp)
        
def HeapSort(V, cmp):
    n = len(V)
    for i in range(n, -1, -1):
        make_heap(V, n, i, cmp)
 
    for i in range(n - 1, 0, -1):
        V.swap(0, i)
        make_heap(V, i, 0, cmp)

def Filter(V, cmp):
    W = MyVector([])
    S = Student(4, "Alexut", 333)
    for i in range(0, len(V)):
        if (cmp(V[i], S)):
            W.push_back(V[i])
    
    
    while len(V) > 0:
        V.__delItem__(0)
    
    for i in range(0, len(W)):
        V.push_back(W[i])
        
V = MyVector([])
V.push_back(Student(1, "Tudor", 914))
V.push_back(Student(3, "Paul", 915))
V.push_back(Student(2, "Alex", 214))
V.push_back(Student(6, "Marius", 912))
V.push_back(Student(4, "Ionut", 913))

HeapSort(V, cmp)
Filter(V, cmp)

print(len(V))

for it in V:
    print(it.get_ID(), it.get_name(), it.get_group())
