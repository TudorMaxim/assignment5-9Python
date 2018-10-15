'''
Created on Nov 6, 2017

@author: Tudor
'''

from predefined_data.my_data import Predef_data
from controller.student_controller import Students
from controller.assignment_controller import Assignments
from controller.grade_controller import Grades
from ui.console import Console
from repository.repository import Repository
from repository.undo_repository import UndoRepository
from controller.undo_controller import UndoController
from repository.StudentCSVRepository import StudentCSVRepository
from repository.AssignmentCSVRepository import AssignmentCSVRepository
from repository.GradeCSVRepository import GradeCSVRepository
from repository.PickleFileRepository import PickleFileRepository

def ReadSettings(repo_type):
    SETTINGS_FILE = None
    if repo_type == 1:
        SETTINGS_FILE = "settings_inmemory.properties"
    elif repo_type == 2:
        SETTINGS_FILE = "settings_CSV.properties"
    elif repo_type == 3:
        SETTINGS_FILE = "settings_binary.properties"
    else:
        return None
    
    f = open(SETTINGS_FILE, "r")
    lines = f.read().split("\n")
    settings = {}
    
    for line in lines:
        setting = line.split("=")
        if len(setting) > 1:
            settings[setting[0]] = setting[1]
            
    f.close()
    return settings


class MyApplication:
    def main(self):
        print("Welcome to my application! Choose the setting file that you want.")
        print("Type: ")
        print("1 for in memory repository")
        print("2 for text files repository")
        print("3 for binary files repository")
        
        repo_type = int(input())
        settings = ReadSettings(repo_type)
        
        if settings == None:
            print("Wrong option!")
            return 1 #EXIT_FAILURE
        
        o = UndoController(UndoRepository())
        r = UndoController(UndoRepository())
            
        if 'CSV' == settings['repository']:
            s = Students(StudentCSVRepository())
            a = Assignments(AssignmentCSVRepository())
            g = Grades(GradeCSVRepository())
            Predef_data(s, a, g)             
            console = Console(s, a, g, o, r)
            console.run_menu()
        
        elif 'binary' == settings['repository']:
            s = Students(PickleFileRepository(settings['students']))
            a = Assignments(PickleFileRepository(settings['assignments']))
            g = Grades(PickleFileRepository(settings['grades']))
            #Predef_data(s, a, g)             
            console = Console(s, a, g, o, r)
            console.run_menu()
        
        else:
            s = Students(Repository())
            a = Assignments(Repository())
            g = Grades(Repository())
            Predef_data(s, a, g)             
            console = Console(s, a, g, o, r)
            console.run_menu()
        
        return 0 #EXIT_SUCCESS
        
  
if __name__ == '__main__':
    app = MyApplication()
    app.main()
    
    
    
    
    
    
    