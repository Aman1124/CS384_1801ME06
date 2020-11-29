import csv
import os


def group_allocation(filename, number_of_groups):
	branches = []
	strength = []
	header = []

	currPath = os.getcwd()
	result_path = os.path.join(currPath, "results")

	try:
		os.mkdir(result_path)
	except:
		pass

	with open(os.path.join(currPath, filename), "r") as file:
		reader = csv.reader(file)
		first = True
		c = 0
		for row in reader:
			if first:
				header = row
				first = False
				continue
			if not row[0][4:6] in branches:
				branches.append(row[0][4:6])
				strength.append(c)
				c = 0
			c += 1

	strength.append(c)
	strength.pop(0)

	for i in range(len(strength)):
		for j in range(len(strength)-i-1):
			if strength[j] < strength[j+1] : 
				strength[j], strength[j+1] = strength[j+1], strength[j]
				branches[j], branches[j+1] = branches[j+1], branches[j]
			
			if strength[j] == strength[j+1] :
				if branches[j] > branches[j+1]:
					strength[j], strength[j+1] = strength[j+1], strength[j]
					branches[j], branches[j+1] = branches[j+1], branches[j]

	branch_strength = {}

	for i in range(len(branches)):
		branch_strength[branches[i].upper()] = strength[i]

	#Creating branch_strength.csv and writing to it
	with open(os.path.join(result_path, "branch_strength.csv"), "w") as file:
		writer = csv.writer(file)
		writer.writerow(["BRANCH_CODE", "STRENGTH"])
		for branch in branches:
			writer.writerow([branch,strength[branches.index(branch)]])

	# print("BRANCHES: ", branch_strength)

	std_details = [[] for _ in range(len(branches))]

	with open(os.path.join(currPath, filename), "r") as file:
		reader = csv.reader(file)
		first = True
		for row in reader:
			if first:
				first = False
				continue
			std_details[branches.index(row[0][4:6])].append(row)

	#Creating BRANCH_NAME.csv files and writing to them
	for i in range(len(branches)):
		f = open(os.path.join(result_path, branches[i].upper() + ".csv"), "w")
		writer = csv.writer(f)
		writer.writerow(["Roll", 'Name', "Email"])
		writer.writerows(std_details[i])


	groups = number_of_groups

	grp_strength = {}
	left = {}

	for i in range(groups):
		tmp = {}
		for branch in branches:
			tmp[branch] = branch_strength[branch.upper()] // groups
		grp_strength[i+1] = tmp

	for branch in branches:
		left[branch] = branch_strength[branch.upper()] % groups 


	last_location = 1

	for branch in branches:
		for i in range(left[branch]):
			grp_strength[last_location][branch] += 1
			last_location += 1
			if last_location > groups:
				last_location = 1

	std_details_copy = std_details


	#Creating Group_G0n.csv and writing the data
	for i in range(groups):
		print("GROUP {:02d}: ".format(i+1), grp_strength[i+1])
		file = open(os.path.join(result_path, "Group_G" + "{:02d}".format(i+1) + ".csv"), "w")
		writer = csv.writer(file)
		writer.writerow(header)
		for j in range(len(branches)):
			for k in range(grp_strength[i+1][branches[j]]):
				writer.writerow(std_details_copy[j][0])
				std_details_copy[j].pop(0)

	stats_csv_header = ['group', 'total']
	for branch in branches:
		stats_csv_header.append(branch)

	with open(os.path.join(result_path, "stats_grouping.csv"), "w") as file:
		writer = csv.writer(file)
		writer.writerow(stats_csv_header)
		for i in range(groups):
			row = ["Group_G" + "{:02d}".format(i+1) + ".csv"]
			grp_total = 0
			for branch in branches:
				grp_total += grp_strength[i+1][branch.upper()]
			row.append(grp_total)
			for branch in branches:
				row.append(grp_strength[i+1][branch.upper()])
			writer.writerow(row)



filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)