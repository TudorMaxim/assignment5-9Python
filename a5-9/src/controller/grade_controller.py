'''
Created on Nov 6, 2017

@author: Tudor
'''
from domain.entities import Grade
from MyVector.MyVector import MyVector, HeapSort


class Grades:
    def __init__(self, repository):
        self.__repository = repository
        
    def get_grades(self):
        return self.__repository.get_all()
    
    def list_given_assignments(self):
        return self.__repository.get_all()
    
    def remove_grade(self, gradeID):
        self.__repository.delete(gradeID)
    
    def make_it_zero(self, gradeID):
        self.__repository.make_zero(gradeID)  
        
       
    def give_assignment_to_student(self, students, assignments, studentID, assignmentID):
        gradeID = int(str(studentID) + str(assignmentID))
        if self.__repository.find_by_id(gradeID) != 0:
            return 2
        if students.exist_student(studentID) == 0:
            return 1
        if assignments.exist_assignment(assignmentID) == 0:
            return 1
        grade = Grade(assignmentID, studentID, 0)
        self.__repository.add(grade)
        return 0
    
    def give_assignment_to_group(self, students, assignments, group, assignmentID):
        exist = False
        l = students.get_students()
        for i in range(0, len(l)):
            if l[i].get_group() == group:
                exist = True
                
        if assignments.exist_assignment(assignmentID) == 0 or exist == False:
            return 1
        
        for i in range(0, len(l)):
            if l[i].get_group() == group:
                gradeID = int(str(l[i].get_ID()) + str(assignmentID))
                if self.__repository.find_by_id(gradeID) == 0:
                    grade = Grade(assignmentID, l[i].get_ID(), 0)
                    self.__repository.add(grade)
        return 0
    
    def remove_assignment_to_group(self, students, assignments, group, assignmentID):
        l = students.get_students()
        for i in range(0, len(l)):
            if l[i].get_group() == group:
                gradeID = int(str(l[i].get_ID()) + str(assignmentID))
                if self.__repository.find_by_id(gradeID) != 0:
                    self.__repository.delete(gradeID)
        return 0
        
    def grade_student(self,assignmentID, studentID, grade):
        gradeID = int(str(studentID) + str(assignmentID))
        if self.__repository.find_by_id(gradeID) == 0:
            return 2
        item = self.__repository.get_item(gradeID) 
        if item.get_grade() != 0:
            return 1
        new_grade = Grade(item.get_assignmentID(), item.get_studentID(), grade)
        self.__repository.assign(gradeID, new_grade)
        return 0
    
    def statistic1_sort_cmp(self, x, y):
        if x.get_grade() < y.get_grade():
            return True
        return False
    
    def statistic1(self, assignmentID):
        l = MyVector([])
        grade = self.__repository.get_all()
        for i in range(0, len(grade)):
            if grade[i].get_assignmentID() == assignmentID:
                l.push_back(grade[i])
        #l = sorted(l, key = lambda grade: grade.get_grade())
        HeapSort(l, self.statistic1_sort_cmp)
        
        return l
    
    def statistic2(self, assignments, day, month, year):
        l = MyVector([])
        grade = self.__repository.get_all()
        for i in range(0, len(grade)):
            asm = assignments.get_assignment(grade[i].get_assignmentID())
            deadline = asm.get_deadline()
            d, m, y = deadline.split(".")
            ok = True
            if y > year and grade[i].get_grade() == 0:
                ok = False
            if y == year and m > month and grade[i].get_grade() == 0:
                ok = False
            if y == year and m == month and d > day and grade[i].get_grade() == 0:
                ok = False
                
            if ok == False:
                l.push_back(grade[i])
                
        return l
    
    def statistic_3_and_4_cmp(self, x, y):
        if x[1] > y[1]:
            return True
        return False
    
    def statistic3(self):
        grade = self.__repository.get_all()
        l = MyVector([])
        sum = {}
        nr = {}
        average = {}
        for i in range(0, len(grade)):
            key = grade[i].get_studentID()
            sum[key] = 0
            nr[key] = 0
            
        for i in range(0, len(grade)):
            key = grade[i].get_studentID()
            sum[key] += grade[i].get_grade()
            nr[key] += 1
        
        for i in range(0, len(grade)):
            key = grade[i].get_studentID()
            average[key] = sum[key] / nr[key]
        
        for key, value in average.items():
            l.push_back([key, value])
        
        #l = sorted(l, key = lambda item : item[1], reverse = True)
        HeapSort(l, self.statistic_3_and_4_cmp)
        return l
    
    def statistic4(self):
        grade = self.__repository.get_all()
        l = MyVector([])
        sum = {}
        nr = {}
        average = {}
        for i in range(0, len(grade)):
            key = grade[i].get_assignmentID()
            sum[key] = 0
            nr[key] = 0
            
        for i in range(0, len(grade)):
            key = grade[i].get_assignmentID()
            sum[key] += grade[i].get_grade()
            nr[key] += 1
        
        for i in range(0, len(grade)):
            key = grade[i].get_assignmentID()
            average[key] = sum[key] / nr[key]
        
        for key, value in average.items():
            if value > 0: l.push_back([key, value])
        
        #l = sorted(l, key = lambda item : item[1], reverse = True)
        HeapSort(l, self.statistic_3_and_4_cmp)
        return l
        
    
    
    
        