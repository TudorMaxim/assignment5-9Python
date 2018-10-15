'''
Created on Nov 6, 2017

@author: Tudor
'''
import unittest
from domain.entities import Assignment
from controller.assignment_controller import Assignments


class AssignmentsTestCase(unittest.TestCase):
    def test_get_assignment(self):
        assignments = Assignments()
        assert assignments.get_assignments() == []
        
    def test_add_assignment(self):
        assignment = Assignment(1, "laboratory 5", "7.11.2017")
        v = [assignment]
        assignments = Assignments()
        assignments.add_assignment(assignment)
        assert(assignments.get_assignments() == v)
        
    def test_remove_assignments(self):
        assignment_1 = Assignment(1, "laboratory 5", "7.11.2017")
        assignment_2 = Assignment(2, "laboratory 6", "10.11.2017")
        assignments_1 = Assignments()
        assignments_2 = Assignments()
        assignments_1.add_assignment(assignment_1)
        assignments_1.add_assignment(assignment_2)
        assignments_2.add_assignment(assignment_1)
        assignments_1.remove_assignment(assignment_2)
        assert assignments_1 == assignments_2
        
    def test_update_assignments(self):
        assignment_1 = Assignment(1, "laboratory 5", "7.11.2017")
        assignment_2 = Assignment(2, "laboratory 6", "10.11.2017")
        assignments_1 = Assignments()
        assignments_2 = Assignments()
        assignments_1.add_assignment(assignment_1)
        assignments_2.add_assignment(assignment_2)
        assignments_2.update_assignment(assignment_2, assignment_1)
        assert assignments_1 == assignments_2
        
    def test_exist_assignment(self):
        assignment = Assignment(1, "laboratory 5", "7.11.2017")
        assignments = Assignments()
        assignments.add_assignment(assignment)
        assert assignments.exist_assignment(1) == True
        assert assignments.exist_assignment(2) == False

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(AssignmentsTestCase))
    return suite