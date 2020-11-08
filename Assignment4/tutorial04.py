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

def create_all_csv():
    with open("acad_res_stud_grades.csv", "r") as file:
        reader = csv.reader(file)
        roll_no = []
        for row in reader:
        	if row[6] in validGrades:
        		roll_no.append(row[1])
        	else:
        		invalidData = True
        # print(len(roll_no))
    roll_no = list(dict.fromkeys(roll_no))
    for r in roll_no:
      	file = open(currPath + "/" + r + "_individual.csv", "w")
      	writer = csv.writer(file)
      	header = [["Roll: " + r,'','','',''],['Semester Wise Details','','','',''],["Subject","Credits","Type","Grade","Sem"]]
      	writer.writerows(header)
      	file.close()
      	file = open(currPath + "/" + r +"_overall.csv", "w")
      	writer = csv.writer(file)
      	header = [["Roll: " + r,'','','','','',''],["Semester","Semester Credits","Semester Credits Cleared","SPI","Total Credits","Total Credits Cleared","CPI"]]
      	writer.writerows(header)
      	file.close()
    if invalidData:
    	file = open(currPath + "/" + "misc.csv", "w")
    	writer = csv.writer(file)
    	header = ['sl','roll','sem','year','sub_code','total_credits','credit_obtained','timestamp','sub_type']

    return roll_no

def write_data_individual(roll_no_data):
	with open("acad_res_stud_grades.csv", "r") as file:
		reader = csv.reader(file)
		p = 0
		c = 1
		data = []
		for row in reader:
			if c == 1:
				c = 2
				continue
			data.append(row)

		i = 0
		while i < len(data):	
			if data[i][6] in validGrades:
				if roll_no_data[p] == data[i][1]:
					file1 = open(currPath + "/" + roll_no_data[p] + "_individual.csv", "a")
					writer = csv.writer(file1)
					rowData = []
					rowData = data[i][4:6]
					rowData.append(data[i][8])
					rowData.append(data[i][6])
					rowData.append(data[i][2])
					writer.writerow(rowData)
				else:
					i -= 1
					p += 1
			else:
				file1 = open(currPath + "/" + "misc.csv", "a")
				writer = csv.writer(file1)
				writer.writerow(data[i])
			i += 1



del_create_grades_folder()
print("del_create_grades_folder() completed")
roll_no = create_all_csv()
print("create_all_csv() completed")
write_data_individual(roll_no)
print("write_data_individual() completed")