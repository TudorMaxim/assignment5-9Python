'''
Created on Nov 6, 2017

@author: Tudor
'''
import unittest
from domain.entities import Student, Assignment, Grade


class StudentTestCase(unittest.TestCase):
    
    def test_student(self):
        student = Student(2351, "Tudor", 914)
        self.assertEqual(student.get_ID(), 2351, "Student get_ID assertion failed")
        self.assertEqual(student.get_name(),  "Tudor", "Student get_Name assertion failed!")
        self.assertEqual(student.get_group(), 914, "Student get_Group assertion failed")
    
        student_2 = Student(1234, "Vlad", 913)
        self.assertEqual(student_2.set_ID(2351), student.get_ID(), "Student set_ID assertion failed!")
        self.assertEqual(student_2.set_name("Tudor"),  student.get_name(), "Student set_name assertion failed!")
        self.assertEqual(student_2.set_group(914), student.get_group(), "student set_group assertion failed!")
    

class AssignmentTestCase(unittest.TestCase):
    def test_assignment(self):
        assignment_1 = Assignment(1, "Lab 1", "10.10.2017")
        self.assertEqual(assignment_1.get_ID(), 1, "Laboratory get_ID assertion failed!")
        self.assertEqual(assignment_1.get_description(), "Lab 1", "Laboratory get_description assertion failed!")
        self.assertEqual(assignment_1.get_deadline(), "10.10.2017", "Laboratory get_deadline assertion failed!")
    
        assignment_2 = Assignment(2, "Lab 2", "17.10.2017")
        self.assertEqual(assignment_2.set_ID(1), assignment_1.get_ID() , "Laboratory set_ID assertion failed!")
        self.assertEqual(assignment_2.set_description("Lab 1"), assignment_1.get_description(), "Laboratory set_description assertion failed!")
        self.assertEqual(assignment_2.set_deadline("10.10.2017"), assignment_1.get_deadline(), "Laboratory set_deadline assertion failed!")

class GradeTestCase(unittest.TestCase):
    def test_grade(self):
        grade_1 = Grade(1, 2, 10)
        self.assertEqual(grade_1.get_assignmentID(), 1, "Grade get_assignment_ID assertion failed!")
        self.assertEqual(grade_1.get_studentID(), 2, "Grade get_student_ID assertion failed!")
        self.assertEqual(grade_1.get_grade(), 10, "Grade get_grade assertion failed!")
        
        grade_2 = Grade(2, 3, 9)
        self.assertEqual(grade_2.set_assignmentID(1), 1, "Grade set_assignment_ID assertion failed!")
        self.assertEqual(grade_2.set_studentID(2), 2, "Grade set_student_ID assertion failed!")
        self.assertEqual(grade_2.set_grade(10), 10, "Grade set_grade assertion failed!")


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StudentTestCase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AssignmentTestCase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GradeTestCase))
    return suite
