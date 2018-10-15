'''
Created on Dec 11, 2017

@author: Tudor
'''
import pickle
from repository.repository import Repository
import repository

class PickleFileRepository(Repository):
    def __init__(self, fileName):
        Repository.__init__(self)
        self._fName = fileName
        self._loadFromFile()
    
    def add(self, client):
        Repository.add(self, client)
        self._storeToFile()
     
    def delete(self, clientId):
        Repository.delete(self, clientId)
        self._storeToFile()        
 
    def update(self, client):
        Repository.update(self, client)
        self._storeToFile()

    def _loadFromFile(self):
        f = open(self._fName, "rb")
        try:
            l = pickle.load(f)
            for s in l:
                Repository.add(self, s)
        except EOFError:
            self._objects = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def _storeToFile(self):
        f = open(self._fName, "wb")
        pickle.dump(self.get_all(), f)
        f.close()