import csv
import os
import shutil
import pandas as ps

os.system("clear")

currPath = os.getcwd()
currPath = os.path.join(currPath, r"grades")
validGrades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'F', 'I']
gradesCredit = [10,9,8,7,6,5,4,0,0]
invalidData = False


def del_create_grades_folder():
    try:
        os.mkdir(currPath)
    except:
        shutil.rmtree(currPath)
        os.mkdir(currPath)
    pass


del_create_grades_folder()
print("del_create_grades_folder() completed")