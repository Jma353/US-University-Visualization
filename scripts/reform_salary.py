#!/usr/bin/env python 

import re # Regular expressions 
import json


def reformat_salaries(): 
	# Open the file 
	with open('../JSONS/archive/salaries.json') as salary_JSON: 
		salary_json = json.load(salary_JSON)

	new_JSON = [] 
	# Loop through each individual school 
	for element in salary_json: 
		# Reformat / curate each JSON
		element_JSON = {} 
		element_JSON["school"] = element["School Name"]
		if "University of Maryland" in element_JSON["school"]: 
			print element["Zip Code"]

		element_JSON["salary_info"] = {} 
		element_JSON["salary_info"]["early_median_salary"] = int(element["Early Career Median Pay"])
		element_JSON["salary_info"]["mid_career_median_salary"] = int(element["Mid-Career Median Pay"])
		element_JSON["salary_info"]["rank"] = int(element["Rank"])
		zip_code = element["Zip Code"] if (len(element["Zip Code"]) == 5) else "0" + element["Zip Code"]
		element_JSON["salary_info"]["zip_code"] = zip_code
		new_JSON.append(element_JSON)

	# Dump this new JSON 
	with open('../JSONS/curated_salaries.json', 'w') as outfile: 
		json.dump(new_JSON, outfile)


reformat_salaries() 