import csv
import os

os.system("cls")

currPath = os.getcwd()
currPath = os.path.join(currPath, r"analytics")
try:
    os.mkdir(currPath)
except:
    pass


def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    pass


def course():
    coursePath = os.path.join(currPath, r"course")
    try:
        os.mkdir(coursePath)
    except:
        pass

    with open("studentinfo_cs384.csv", "r") as file:
        reader = csv.reader(file)
        data = []
        invalidData = []
        rollNo = []
        for row in reader:
            if (
                not len(row[0]) == 8
                or not str.isnumeric(row[0][0:4])
                or not str.isalpha(row[0][4:6])
                or not str.isnumeric(row[0][6:])
            ):
                invalidData.append(row)
            else:
                data.append(row)
                rollNo.append(row[0])

    with open(os.path.join(coursePath, r"misc.csv"), "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(invalidData)

    branches = []

    for courseCode in rollNo:
        if not os.path.exists(os.path.join(coursePath, courseCode[4:6].lower())):
            os.mkdir(os.path.join(coursePath, courseCode[4:6].lower()))
            branches.append(courseCode[4:6])

    for branch in branches:
        for x in data:
            if x[0][4:6] == branch:
                if x[0][2:4] == "01":
                    courseName = "btech"
                elif x[0][2:4] == "11":
                    courseName = "mtech"
                elif x[0][2:4] == "12":
                    courseName = "msc"
                elif x[0][2:4] == "21":
                    courseName = "phd"
                try:
                    os.mkdir(os.path.join(coursePath, branch, courseName))
                except:
                    pass
                finally:
                    fileName = (
                        x[0][0:2] + "_" + branch.lower() + "_" + courseName + ".csv"
                    )
                    openMode = ""
                    if os.path.exists(
                        os.path.join(coursePath, branch, courseName, fileName)
                    ):
                        openMode = "a"
                    else:
                        openMode = "w"
                    with open(
                        os.path.join(coursePath, branch, courseName, fileName),
                        openMode,
                        newline="",
                    ) as file:
                        writer = csv.writer(file)
                        writer.writerow(x)
                        file.close()

    pass


def country():
    countryPath = os.path.join(currPath, r"country")
    try:
        os.mkdir(countryPath)
    except:
        pass

    with open("studentinfo_cs384.csv", "r") as file:
        reader = csv.reader(file)
        countries = []
        a = True
        for row in reader:
            if a:
                a = False
                continue
            openMode = ""
            if os.path.exists(os.path.join(countryPath, row[2].lower())):
                openMode = "w"
                countries.append(row[2].lower())
            else:
                openMode = "a"
            with open(
                os.path.join(countryPath, row[2].lower() + ".csv"), openMode, newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow(row)
                file.close()

    pass


def email_domain_extract():
    mailPath = os.path.join(currPath, r"email_domain")
    try:
        os.mkdir(mailPath)
    except:
        pass

    with open("studentinfo_cs384.csv", "r") as file:
        reader = csv.reader(file)
        a = True
        for row in reader:
            if a:
                a = False
                continue
            openMode = ""
            domain = ((row[3].split("@"))[1].split("."))[0]
            if os.path.exists(os.path.join(mailPath, domain)):
                openMode = "w"
            else:
                openMode = "a"
            with open(
                os.path.join(mailPath, domain + ".csv"), openMode, newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow(row)
                file.close()

    pass


def gender():
    genderPath = os.path.join(currPath, r"gender")
    try:
        os.mkdir(genderPath)
    except:
        pass

    with open("studentinfo_cs384.csv", "r") as file:
        reader = csv.reader(file)
        a = True
        for row in reader:
            if a:
                a = False
                continue
            openMode = ""
            if os.path.exists(os.path.join(genderPath, row[4].lower())):
                openMode = "w"
            else:
                openMode = "a"
            with open(
                os.path.join(genderPath, row[4].lower() + ".csv"), openMode, newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow(row)
                file.close()

    pass


def dob():
    # Read csv and process
    pass


def state():
    statePath = os.path.join(currPath, r"state")
    try:
        os.mkdir(statePath)
    except:
        pass

    with open("studentinfo_cs384.csv", "r") as file:
        reader = csv.reader(file)
        a = True
        for row in reader:
            if a:
                a = False
                continue
            openMode = ""
            if os.path.exists(os.path.join(statePath, row[7].lower())):
                openMode = "w"
            else:
                openMode = "a"
            with open(
                os.path.join(statePath, row[7].lower() + ".csv"), openMode, newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow(row)
                file.close()

    pass


def blood_group():
    bloodPath = os.path.join(currPath, r"blood_group")
    try:
        os.mkdir(bloodPath)
    except:
        pass

    with open("studentinfo_cs384.csv", "r") as file:
        reader = csv.reader(file)
        a = True
        for row in reader:
            if a:
                a = False
                continue
            openMode = ""
            if os.path.exists(os.path.join(bloodPath, row[6].lower())):
                openMode = "w"
            else:
                openMode = "a"
            with open(
                os.path.join(bloodPath, row[6].lower() + ".csv"), openMode, newline=""
            ) as file:
                writer = csv.writer(file)
                writer.writerow(row)
                file.close()

    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass


course()
country()
gender()
state()
blood_group()
email_domain_extract()