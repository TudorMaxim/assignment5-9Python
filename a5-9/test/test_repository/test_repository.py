'''
Created on Nov 21, 2017

@author: Tudor
'''
import unittest
from domain.entities import Student
from repository.repository import Repository

class RepositoryTestCase(unittest.TestCase):
    
    
    def test_add(self):
        student = Student(1, "Tudor", 914)
        x = {1:student}
        repository = Repository()
        repository.add(student)
        self.assertEqual(repository.get_all(), list(x.values()), "Repository add assertion error!")
        
    def test_delete(self):
        repository = Repository()
        student = Student(1, "Tudor", 914)
        repository.add(student)
        repository.delete(1)
        self.assertEqual(repository.get_all(), [], "Repository delete assertion error!")
        
    def test_update(self):
        repository = Repository()
        student = Student(1, "Tudor", 914)
        new_student = Student(1, "Tudor Maxim", 914)
        repository.add(student)
        repository.update(new_student)
        self.assertEqual(repository.find_by_id(1), new_student, "Repository update assertion error!")
        
    def test_size(self):
        repository = Repository()
        repository.add(Student(1, "Tudor", 914))
        self.assertEqual(repository.size(), 1, "Repository size assertion error!")
        
    def test_get_all(self):
        repository = Repository()
        student = Student(1, "tudor", 914)
        l = [student]
        repository.add(student)
        self.assertEqual(repository.get_all(), l, "Repository get_all assertion error!")
        
    def test_get_item(self):
        repo = Repository()
        student = Student(1, "tudor", 914)
        repo.add(student)
        self.assertEqual(repo.get_item(1), student, "Repository get_item assertion error!")
        
    def tetst_find_by_id(self):
        repo = Repository()
        student = Student(1, "tudor", 914)
        repo.add(student)
        self.assertEqual(repo.find_by_id(1), student, "Repository find_by_id assertion error!")
        self.assertEqual(repo.find_by_id(2), 0, "Repository find_by_id assertion error!")
         
def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RepositoryTestCase))
    return suite