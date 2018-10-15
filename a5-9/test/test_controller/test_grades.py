'''
Created on Nov 6, 2017

@author: Tudor
'''
import unittest
from domain.entities import Grade, Student, Assignment
from controller.grade_controller import Grades
from controller.student_controller import Students
from controller.assignment_controller import Assignments

class GradesTestCase(unittest.TestCase):
    def test_get_grades(self):
        grades = Grades()
        assert grades.get_grades() == []
    
    def test_add_grades(self):
        grade = Grade(1, 2, 10)
        v = [grade]    
        grades = Grades()
        grades.add_grades(grade)
        assert grades.get_grades() == v
        
    def test_check_existence(self):
        grade = Grade(1, 2, 10)
        grades = Grades()
        grades.add_grades(grade)
        assert grades.check_existence(1, 2) == False
        assert grades.check_existence(2, 1) == True
        
    def test_give_assignment_to_student(self):
        students = Students()
        assignments = Assignments()
        ans = [Grade(1, 1, 0)]
        grades = Grades()
        student = Student(1, "Tudor", 914)
        assignment = Assignment(1, "laboratory 1", "7.10.2017")
        students.add_student(student)
        assignments.add_assignment(assignment)
        grades.give_assignment_to_student(students, assignments, 1, 1)
        assert grades.get_grades() == ans
        
    def test_give_assignments_to_group(self):
        students = Students()
        assignments = Assignments()
        grades = Grades()
        ans = [Grade(1, 1, 0)]
        student = Student(1, "Tudor", 914)
        assignment = Assignment(1, "laboratory 1", "7.10.2017")
        students.add_student(student)
        assignments.add_assignment(assignment)
        grades.give_assignment_to_group(students, assignments, 914, 1)
        assert grades.get_grades() == ans

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(GradesTestCase))
    return  suite