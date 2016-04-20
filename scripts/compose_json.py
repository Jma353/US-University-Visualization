#!/usr/bin/env python 

import re # Regular expressions 
import json

# Obtain the scores.json file + corresponding JSON 
with open('../JSONS/scores.json') as score_JSON: 
	score_json = json.load(score_JSON)

# Obtain the curated_salaries.json + corresponding JSON 
with open('../JSONS/curated_salaries.json') as salary_JSON: 
	salary_json = json.load(salary_JSON)

# Obtain the admissions.json + corresponding JSON 
with open('../JSONS/admissions.json') as admissions_JSON: 
	admissions_json = json.load(admissions_JSON)


overall_json = []

for i in score_json: 
	for j in salary_json: 
		if (j["school"] in i["school"]) or (i["school"] in j["school"]): 
			element = {} 
			element["score_JSON"] = i 
			element["salary_JSON"] = j 
			overall_json.append(element)

for lol_json in overall_json: 
	print lol_json




# inJorK = (j["school"] in k["school"]) or (k["school"] in j["school"])
# inIorK = (k["school"] in i["school"]) or (i["school"] in k["school"])