#!/usr/bin/env python 

import re # Regular expressions 
import json

# Obtain the scores.json file + corresponding JSON 
with open('../scores.json') as score_JSON: 
	score_json = json.load(score_JSON)

# Obtain the salaries.json, p bloated 
with open('../salaries.json') as salary_JSON: 
	salary_json = json.load(salary_JSON)

for i in salary_json: 
	print i['School Name']