import json
import csv
import io

def read_csv_file(filename):
        """
        Read the contents of a CSV file and return it as a list of dictionaries using the keys
        specified in the first line of the file.
        """
        with open(filename, 'r', encoding='UTF-8') as csv_file:
            return [row for row in csv.DictReader(csv_file, delimiter=';', quotechar='"')]

redpoint_database = {"categories": []}

redpoint_database_raw = read_csv_file("./Numbers Export/Training-Table 1.csv")

current_category = {}

for line in redpoint_database_raw:
	if line["Category"] != "":
		current_category = {}
		current_category["name"] = line["Category"]
		current_category["color"] = line["Color"]
		current_category["imageName"] = line["Category"]
		current_category["trainings"] = []
		redpoint_database["categories"].append(current_category)
	elif line["Training"] != "":
		current_training = {}
		current_training["name"] = line["Training"]
		current_training["instructions"] = line["Instructions"].split("\n")
		current_training["teaser"] = line["Teaser"]
		current_training["identifier"] = line["Identifier"]
		current_category["trainings"].append(current_training)


index = 1
for category in redpoint_database["categories"]:
	categoryname = category["name"]
	foldername = str(index) + "-" + categoryname
	for instruction in category["trainings"]:
		instructionidentifier = instruction["identifier"]
		if instructionidentifier:
			instructionname = instruction["name"]
			instructionteaser = instruction["teaser"]
			instructiontext = "\n".join(instruction["instructions"])
			content = instructionname + "\n" + instructionteaser + "\n" + instructiontext
			with open("./en/"+foldername+"/"+instructionidentifier+".txt", "w") as text_file:
				text_file.write(content)
	index+=1
    
    
    
