#!/usr/bin/env python 

import re # Regular expressions 
import json

def compose_JSON(): 
	# Obtain the scores.json file + corresponding JSON 
	with open('../JSONS/scores.json') as score_JSON: 
		score_json = json.load(score_JSON)

	# Obtain the curated_salaries.json + corresponding JSON 
	with open('../JSONS/curated_salaries.json') as salary_JSON: 
		salary_json = json.load(salary_JSON)

	# Obtain the admissions.json + corresponding JSON 
	with open('../JSONS/admissions.json') as admissions_JSON: 
		admissions_json = json.load(admissions_JSON)

	# Start forming the json with intersecting elements 
	overall_json = []
	# Intersect score and salary 
	for i in score_json: 
		for j in salary_json: 
			if (j["school"] in i["school"]) or (i["school"] in j["school"]): 
				element = { "school": i["school"] } 
				element["score_JSON"] = i
				element["salary_JSON"] = j 
				overall_json.append(element)


	# At this point, have intersection of SCORES and SALARIES; need ADMISSIONS 

	# Start forming the json with finalized, interesected JSONs 
	final_json = []
	# Intersect overall and admissions  
	for i in overall_json: # i represents overall 
		for j in admissions_json: 
			if (j["school"] in i["school"]) or (i["school"] in j["school"]): 
				element = { "school": i["school"] }

				# score JSON addition 
				score_JSON = i["score_JSON"].copy()
				score_JSON.pop("school", 0)
				element.update(score_JSON)

				# salary JSON addition 
				salary_JSON = i["salary_JSON"].copy() 
				salary_JSON.pop("school", 0)
				element.update(salary_JSON)

				# admission JSON addition 
				admissions_JSON = j.copy() 
				admissions_JSON.pop("school", 0)
				element.update(admissions_JSON)

				# Add the refined JSON 
				final_json.append(element)


	# dump final_json to file 
	with open("../schools.json", "w") as outfile: 
		json.dump(final_json, outfile)



compose_JSON() 




