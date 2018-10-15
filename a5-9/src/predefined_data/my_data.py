'''
Created on Nov 6, 2017

@author: Tudor
'''
from domain.entities import Student, Assignment

def Predef_data(students, assignments, grades):
    student = Student(1, "Tudor", 914)
    students.add_student(student)
    student = Student(2, "Vlad", 911)
    students.add_student(student)
    student = Student(4, "David", 912)
    students.add_student(student)
    student = Student(3, "Stefan", 912)
    students.add_student(student)
    student = Student(5, "Dragos", 914)
    students.add_student(student)
    student = Student(6, "Ionut", 911)
    students.add_student(student)
    student = Student(7, "Alexandra", 911)
    students.add_student(student)
    student = Student(8, "Eliza", 913)
    students.add_student(student)
    student = Student(9, "Stefana", 913)
    students.add_student(student)
    student = Student(10, "Teodora", 915)
    
    assignment = Assignment(1, "laboratory 1", "10.10.2017")
    assignments.add_assignment(assignment)
    assignment = Assignment(2, "laboratory 2", "17.10.2017")
    assignments.add_assignment(assignment)
    assignment = Assignment(3, "laboratory 3", "22.10.2017")
    assignments.add_assignment(assignment)
    assignment = Assignment(4, "laboratory 4", "4.11.2017")
    assignments.add_assignment(assignment)
    assignment = Assignment(5, "laboratory 5", "14.11.2017")
    assignments.add_assignment(assignment)
    assignment = Assignment(6, "laboratory 6", "28.11.2017")
    assignments.add_assignment(assignment)
    
    
    grades.give_assignment_to_student(students, assignments, 1, 1)
    grades.give_assignment_to_group(students, assignments, 914, 3)
    grades.give_assignment_to_group(students, assignments, 912, 2)
    grades.grade_student(1, 1, 10)
    grades.grade_student(3, 1, 9)
    grades.grade_student(3, 5, 8)
    grades.grade_student(2, 4, 9)
    grades.grade_student(2, 3, 7)
    
