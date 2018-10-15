'''
Created on Nov 6, 2017

@author: Tudor
'''
from domain.entities import Student, Assignment
import sys

class Console:
    def __init__(self, students, assignments, grades, operations, redo_operations):
        self.__students = students
        self.__assignments = assignments
        self.__grades = grades
        self.__operations = operations
        self.__redo_operations = redo_operations
    
    def ui_add_student(self):
        try:
            studentID = int(input("Give the student's ID: "))
            name = input("Give the student's name: ")
            group = int(input("Give the student's group: "))
            student = Student(studentID, name, group)
            error = self.__students.add_student(student)
            if group < 1:
                print("the group must be natural numbers > 0")
            else:
                if error == 1:
                    print ("A student with the given ID already exists!")
                else:
                    self.__operations.add((1, [student]))
        except ValueError:
            print("The ID and the group must be natural numbers > 0")
    
    def ui_add_assignment(self):
        try:
            assignmentID = int(input("Give the assignment's ID: "))
            description = input("Give the assignment's description: ")
            deadline = input("Give the assignment's deadline: ")
            assignment = Assignment(assignmentID, description, deadline)
            error = self.__assignments.add_assignment(assignment)
            if error == 1:
                print("An assignment with the given ID already exists!")
            else:
                self.__operations.add((5, [assignment]))
        except Exception:
            print("The ID must be a natural number > 0")
    
    def ui_remove_student(self):
        try:
            studentID = int(input("Give the student's ID: "))
            name = input("Give the student's name: ")
            group = int(input("Give the student's group: "))
            student = Student(studentID, name, group)
            error = self.__students.remove_student(student)
            if error == 1:
                print("The student does not exist!")
            else:  
                self.ui_delete_student_grade(student)
                self.__operations.add((2, [student])) 
        except ValueError:
            print("The ID and the group must be natural numbers > 0")
            
    
    def ui_remove_assignment(self):
        try:
            assignmentID = int(input("Give the assignment's ID: "))
            description = input("Give the assignment's description: ")
            deadline = input("Give the assignment's deadline: ")
            assignment = Assignment(assignmentID, description, deadline)
            error = self.__assignments.remove_assignment(assignment)
            if error == 1:
                print("The assignment does not exist!")
            else:
                self.ui_delete_assignment_grade(assignment)
                self.__operations.add((6, [assignment]))
        except ValueError:
            print("The ID must be a natural number > 0")
    
    def ui_update_student(self):
        try:
            studentID = int(input("Give the student's ID: "))
            name = input("Give the student's name: ")
            group = int(input("Give the student's group: "))
            student = Student(studentID, name, group)
            new_studentID = int(input("Give the new ID: "))
            new_name = input("Give the new name: ")
            new_group = int(input("Give the new group: "))
            new_student = Student(new_studentID, new_name, new_group)
            error = self.__students.update_student(student, new_student)
            if error == 1:
                print("There is no student with this ID")
            else:
                self.__operations.add((3, [student, new_student]))  
        except ValueError:
            print("The ID and the group must be natural numbers > 0")
            
    
    def ui_update_assignment(self):
        try:
            assignmentID = int(input("Give the assignment's ID: "))
            description = input("Give the assignment's description: ")
            deadline = input("Give the assignment's deadline: ")
            assignment = Assignment(assignmentID, description, deadline)
            
            new_assignmentID = int(input("Give the new ID: "))
            new_description = input("Give the new description: ")
            new_deadline = input("Give the new deadline: ")
            new_assignment = Assignment(new_assignmentID, new_description, new_deadline)
            
            error = self.__assignments.update_assignment(assignment, new_assignment)
            if error == 1:
                print("There is no student with this ID")
            else:
                self.__operations.add((7, [assignment, new_assignment]))
        except ValueError:
            print("The ID must be natural numbers > 0")
            
            
    def ui_list_students(self):
        l = self.__students.get_students()
        if len(l) == 0:
            print("The are no students registered!")
        else:
            print("The list of students is: ")
            for i in range(0, len(l)):
                print(l[i].get_ID(), l[i].get_name(), l[i].get_group())
    
    def ui_list_assignments(self):
        l = self.__assignments.get_assignments()
        if len(l) == 0:
            print("The are no assignments registered!")
        else:
            print("The list of assignments is: ")
            for i in range(0, len(l)):
                print(l[i].get_ID(), l[i].get_description(), l[i].get_deadline())
    
    def ui_give_assignment_to_student(self):
        try:
            assignmentID = int(input("Give the assignment's ID: "))
            studentID = int(input("Give the student's ID: "))
            error = self.__grades.give_assignment_to_student(self.__students, self.__assignments, studentID, assignmentID)
            if error == 1:
                print("The student or the assignment does not exist! ")
            elif error == 2:
                print("This student already has this assignment!")
            else:
                self.__operations.add((9, [assignmentID, studentID]))
        except ValueError:
            print("The ID must be a number")
    
    def ui_give_assignment_to_group(self):
        try:
            assignmentID = int(input("Give the assignment's ID: "))
            group = int(input("Give the group: "))
            error = self.__grades.give_assignment_to_group(self.__students, self.__assignments, group, assignmentID)
            if error == 1:
                print("The group or the assignment does not exist! ")
            else:
                self.__operations.add((10, [group, assignmentID]))
        except ValueError:
            print("The ID and the group must be numbers")
            
    def ui_list_given_assignments(self):
        l = self.__grades.list_given_assignments()
        if len(l) == 0:
            print("The are no assignments given to any student!")
        else:
            for i in range(0, len(l)):
                #print(i.get_assignmentID(), i.get_studentID(),  i.get_grade())
                std = self.__students.get_student(l[i].get_studentID())
                asm = self.__assignments.get_assignment(l[i].get_assignmentID())
                print ("Student", l[i].get_studentID(), "named", std.get_name(), "from group", std.get_group(), 
                       "has assignment", l[i].get_assignmentID(), "with deadline", asm.get_deadline(), "and is graded with ", l[i].get_grade())
    
    def ui_grade_student(self):
        try:
            assignmentID = int(input("Give the ID of the assignment that you want to grade: "))
            studentID = int(input("Give the ID of the student that you want to grade: "))
            grade = int(input("Give the grade: "))
            error = self.__grades.grade_student(assignmentID, studentID, grade)
            if error == 1:
                print("This assignment for the given student is already graded")
            elif error == 2:
                print("This student does not have the given assignment")
            else:
                self.__operations.add((12, [assignmentID, studentID, grade]))
        except ValueError:
            print("the ID's and the grades must be numbers")
            
    def ui_delete_student_grade(self, student):
        for i in self.__grades.get_grades():
            if i.get_studentID() == student.get_ID():
                gradeID = int(str(i.get_studentID()) + str(i.get_assignmentID()))
                self.__grades.remove_grade(gradeID)
    
    def ui_delete_assignment_grade(self, assignment):
        for i in self.__grades.get_grades():
            if i.get_assignmentID() == assignment.get_ID():
                gradeID = int(str(i.get_studentID()) + str(i.get_assignmentID()))
                self.__grades.remove_grade(gradeID)
    
    def ui_statistic1(self):
        try:
            assignmentID = int(input("Give assignment ID: "))
            l = self.__grades.statistic1(assignmentID)
            if len(l) == 0:
                print("No student received this assignment")
            for i in l:
                #print(i.get_assignmentID(), i.get_studentID(), i.get_grade())
                std = self.__students.get_student(i.get_studentID())
                asm = self.__assignments.get_assignment(i.get_assignmentID())
                print ("Student", i.get_studentID(), "named", std.get_name(), "from group", std.get_group(), 
                       "has assignment", i.get_assignmentID(), "with deadline", asm.get_deadline(), "and is graded with ", i.get_grade())
        except ValueError:
            print("The ID must be a natural number")
    
    def ui_statistic2(self):
        try:
            date = input("Give the deadline: ")
            day, month, year = date.split(".")
            l = self.__grades.statistic2(self.__assignments, day, month, year)
            if len(l) == 0:
                print("No late assignments")
            else:
                print("The late students with the given assignments are: ")
                for i in l:
                    std = self.__students.get_student(i.get_studentID())
                    asm = self.__assignments.get_assignment(i.get_assignmentID())
                    print(std.get_name(), "with", asm.get_description() )
                    #print(i.get_assignmentID(), i.get_studentID(), i.get_grade())
        except ValueError:
            print("The day, month, and year of the date must be natural numbers")
    
    def ui_statistic3(self):
        l = self.__grades.statistic3()
        for i in l:
            std = self.__students.get_student(i[0])
            #print(i[0], i[1])
            print(std.get_name(), "with average grade", i[1])
    
    def ui_statistic4(self):
        l = self.__grades.statistic4()
        if len(l):
            print("No assignments were graded")
        for i in l:
            asm = self.__assignments.get_assignment(i[0])
            print(asm.get_description(), "with average grade", i[1])
    
    def ui_create_statistics(self):
        #statistic = {1: self.ui_statistic1, 2: self.ui_statistic2, 3:self.ui_statistic3, 4:self.ui_statistic4 }
        op = int(input("choose a statistic type: "))
        if op < 1 or op > 4:
            print("Statistics are of type 1, 2, 3 and 4")
            
        if op == 1: self.ui_statistic1()
        if op == 2: self.ui_statistic2()
        if op == 3: self.ui_statistic3()
        if op == 4: self.ui_statistic4()
     
    def ui_undo(self):
        op = self.__operations.get_last()
        if op == 0:
            print("Cannot undo right now!")
        else:
            if op[0] == 1: #Undo an add student
                self.__students.remove_student(op[1][0])
                
            if op[0] == 2:#Undo a remove student
                self.__students.add_student(op[1][0])
            
            if op[0] == 3: #Undo an update student
                self.__students.update_student(op[1][1], op[1][0])
                
            if op[0] == 5: #Undo an add assignment
                self.__assignments.remove_assignment(op[1][0])
            
            if op[0] == 6: #Undo a remove assignment
                self.__assignments.add_assignment(op[1][0])
                
            if op[0] == 7: #Undo an update assignment
                self.__assignments.update_assignment(op[1][1], op[1][0])
                
            if op[0] == 9: #Undo giving an assignment to a student
                gradeID = int(str(op[1][1]) + str(op[1][0]))
                self.__grades.remove_grade(gradeID)
            
            if op[0] == 10: #Undo giving an assignment to a group of students
                self.__grades.remove_assignment_to_group(self.__students, self.__assignments, op[1][0], op[1][1])
            
            if op[0] == 12: #Undo grading a student
                gradeID = int(str(op[1][0]) + str(op[1][1]))
                self.__grades.make_it_zero(gradeID)
                
            self.__redo_operations.add(op)
            self.__operations.pop()
    
    def ui_redo(self):
        op = self.__redo_operations.get_last()
        if op == 0:
            print("Cannot redo right now!")
        else:
            if op[0] == 1: #Redo an add student
                self.__students.add_student(op[1][0])
                
            if op[0] == 2:#Redo a remove student
                self.__students.remove_student(op[1][0])
            
            if op[0] == 3: #Redo an update student
                self.__students.update_student(op[1][0], op[1][1])
                
            if op[0] == 5: #Redo an add assignment
                self.__assignments.add_assignment(op[1][0])
            
            if op[0] == 6: #Redo a remove assignment
                self.__assignments.remove_assignment(op[1][0])
                
            if op[0] == 7: #Redo an update assignment
                self.__assignments.update_assignment(op[1][0], op[1][1])
                
            if op[0] == 9: #Redo giving an assignment to a student
                self.__grades.give_assignment_to_student(self.__students, self.__assignments, op[1][1], op[1][0])
            
            if op[0] == 10: #Redo giving an assignment to a group of students
                self.__grades.give_assignment_to_group(self.__students, self.__assignments, op[1][0], op[1][1])
            
            if op[0] == 12: #Redo grading a student
                self.__grades.grade_student(op[1][1], op[1][0], op[1][2])
                
            self.__operations.add(op)
            self.__redo_operations.pop()
           
    def exit_console(self):
        sys.exit()
    
    def print_options(self):
        print("The options are: ")
        print("0 - exit the application")
        print("1 - add a student")
        print("2 - remove a student")
        print("3 - update a student")
        print("4 - list the students")
        print("5 - add an assignment")
        print("6 - remove an assignment")
        print("7 - update an assignment")
        print("8 - list the assignments")
        print("9 - give an assignment to a student")
        print("10 - give an assignment to a group of students")
        print("11 - list the grades for given assignments to students")
        print("12 - grade a student for an assignment")
        print("13 - Create statistics")
        print("14 - Undo")
        print("15 - Redo")
        
    def run_menu(self):
        options = { 0: self.exit_console,
                    1: self.ui_add_student, 2: self.ui_remove_student, 3: self.ui_update_student, 4: self.ui_list_students,
                    5: self.ui_add_assignment, 6: self.ui_remove_assignment, 7: self.ui_update_assignment, 8: self.ui_list_assignments, 
                    9: self.ui_give_assignment_to_student, 10: self.ui_give_assignment_to_group, 11: self.ui_list_given_assignments,
                    12: self.ui_grade_student, 13: self.ui_create_statistics,
                    14: self.ui_undo, 15: self.ui_redo }
        self.print_options()
        while True:
            try:
                option = int(input("Choose an option: "))
                options[option]()
            except ValueError:
                print("Wrong option!")
            except KeyError:
                print("Wrong option!")
                
