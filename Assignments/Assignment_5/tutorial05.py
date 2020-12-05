import os
import re


dir_path = os.path.join(os.getcwd(), "Subtitles")
global seasonPadding, episodePadding


def rename_FIR(folder_name):
    os.chdir(os.path.join(dir_path, "FIR"))
    files = os.listdir(os.getcwd())
    for file in files:
    	numbers = re.findall("\d+", file)
    	epName = re.split("\.", file)
    	# print(numbers)
    	epNumber = numbers[0].zfill(episodePadding)
    	# sNumber = numbers[0].zfill(seasonPadding)
    	newName = "FIR - Episode " + epNumber + "." + epName[-1]
    	os.rename(file, newName)
    	# print(newName) 
    

def rename_Game_of_Thrones(folder_name):
    os.chdir(os.path.join(dir_path, "Game of Thrones"))
    files = os.listdir(os.getcwd())
    for file in files:
    	numbers = re.findall("\d+", file)
    	epName = re.split("\-|\.", file)
    	# print(epName)
    	epNumber = numbers[1].zfill(episodePadding)
    	sNumber = numbers[0].zfill(seasonPadding)
    	newName = epName[0] + "- Season " + sNumber + " Episode " + epNumber + " -" + epName[2] + "." + epName[-1]
    	os.rename(file, newName)
    	# print(newName)
    

def rename_Sherlock(folder_name):
    os.chdir(os.path.join(dir_path, "Sherlock"))
    files = os.listdir(os.getcwd())
    for file in files:
    	numbers = re.findall("\d+", file)
    	newName = "Sherlock Season " + numbers[0].zfill(seasonPadding) + " Episode " + numbers[1].zfill(episodePadding)
    	if numbers[-1] == '4':
    		os.rename(file, newName + ".mp4")
    	else:
    		os.rename(file, newName + ".srt")

def rename_Suits(folder_name):
	os.chdir(os.path.join(dir_path, "Suits"))
	files = os.listdir(os.getcwd())
	for file in files:
		numbers = re.findall("\d+", file)
		epName = re.split("\-|\.", file)
		# print(epName)
		epNumber = numbers[1].zfill(episodePadding)
		sNumber = numbers[0].zfill(seasonPadding)
		newName = epName[0] + "- Season " + sNumber + " Episode " + epNumber + " -" + epName[2] + "." + epName[-1]
		os.rename(file, newName)
		# print(newName) 
    

def rename_How_I_Met_Your_Mother(folder_name):
    os.chdir(os.path.join(dir_path, "How I Met Your Mother"))
    files = os.listdir(os.getcwd())
    for file in files:
    	numbers = re.findall("\d+", file)
    	epName = re.split("\-|\.", file)
    	# print(epName)
    	epNumber = numbers[1].zfill(episodePadding)
    	sNumber = numbers[0].zfill(seasonPadding)
    	newName = epName[0] + "- Season " + sNumber + " Episode " + epNumber + " -" + epName[2] + "." + epName[-1]
    	os.rename(file, newName)
    	# print(newName) 

print("List of web series:\n1.Sherlock\n2.Game of Thrones\n3.How I Met Your Mother\n4.Suits\n5.FIR")
seriesName = int(input("Enter the number of the Web Series: "))
seasonPadding = int(input('Season Number Padding: '))
episodePadding = int(input("Episode Number Padding: "))


if seriesName == 1:
	rename_Sherlock('Sherlock')
elif seriesName == 2:
	rename_Game_of_Thrones('Game of Thrones')
elif seriesName == 3:
	rename_How_I_Met_Your_Mother('How I Met Your Mother')
elif seriesName == 4:
	rename_Suits('Suits')
elif seriesName == 5:
	rename_FIR('FIR')