'''
Created on Nov 6, 2017

@author: Tudor
'''
import unittest
from domain.entities import Student
from controller.student_controller import Students

class StudentsTestCase(unittest.TestCase):
     
    def test_get_students(self):
        students = Students()
        assert (students.get_students() == [])
        
    def test_add_students(self):
        student = Student(2351, "Tudor", 914)
        students_1 = [student]
        students_2 = Students()
        students_2.add_student(student)
        assert (students_2.get_students() == students_1)
    
    def test_remove_student(self):
        students_1 = Students()
        students_2 = Students()
        a = Student(1, "Tudor", 914)
        b = Student(2, "Dragos", 914)
        students_1.add_student(a)
        students_1.add_student(b)
        students_1.remove_student(b)
        students_2.add_student(a)
        assert(students_1 == students_2)
         
    def test_update_student(self):
        student = Student(1, "Tudor", 914)
        new_student = Student(1, "Maxim Tudor", 914)
        students_1 = Students()
        students_2 = Students()
        students_1.add_student(student)
        students_2.add_student(new_student)
        students_1.update_student(student, new_student)
        assert(students_1 == students_2)
        
    def test_exist_student(self):
        a = Student(1, "Tudor", 914)
        b = Student(2, "Alex", 214)
        students = Students()
        students.add_student(a)
        students.add_student(b)
        assert(students.exist_student(1) == True)
        assert(students.exist_student(2) == True)
        assert(students.exist_student(3) == False)
        
    def test_exist_group(self):
        a = Student(1, "Tudor", 914)
        b = Student(2, "Alex", 214)
        students = Students()
        students.add_student(a)
        students.add_student(b)
        assert(students.exist_group(914) == True)
        assert(students.exist_group(214) == True)
        assert(students.exist_group(924) == False)    

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(StudentsTestCase))
    return suite