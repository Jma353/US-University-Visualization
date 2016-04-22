#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json

# Score processing helper functions 

def score_result(score): 
	if (score != "NA" and "\u2013" not in score):
		score = int(score)
	else: 
		score = "NA"
	return score


def process_split(score): 
	result = score.split("-")
	return_result = (result[0], result[0]) if (len(result) == 1) else (result[0], result[1])
	return return_result


def process_score(sat_math, sat_reading, act):
	# Process SAT math 
	low_math, high_math = process_split(sat_math)
	low_math = score_result(low_math)
	high_math = score_result(high_math)

	# Process SAT reading 
	low_reading, high_reading = process_split(sat_reading)
	low_reading = score_result(low_reading)
	high_reading = score_result(high_reading)

	# Process ACT 
	low_act, high_act = process_split(act)
	low_act = score_result(low_act)
	high_act = score_result(high_act)

	return (low_math, high_math, low_reading, high_reading, low_act, high_act)



def get_scores(): 
	page = r.get("https://www.powerscore.com/sat/help/average_test_scores.cfm")
	tree = html.fromstring(page.content)
	schools = tree.xpath('//table[@id="collegestats"]/tbody/tr/td/b/text()')
	stats = tree.xpath('//table[@id="collegestats"]/tbody/tr/td/text()')
	schools.remove('\r\n   ') # Remove the stray empty value from the scrape 
	school_jsons = []
	for i in range(len(schools)):
		school_JSON = {} 
		school_JSON["school"] = re.sub(' +', ' ', schools[i]) + "" # Clean up extraneous spaces 
		school_JSON["scores"] = {}

		# Grab specific ranges or `NA`'s; replace non-ascii characters 
		sat_math = re.sub(r'[^\x00-\x7F]+','-', stats[i*3])
		sat_reading = re.sub(r'[^\x00-\x7F]+','-', stats[i*3+1])
		act = re.sub(r'[^\x00-\x7F]+','-', stats[i*3+2])

		# Bulk assign these values
		low_math, high_math, low_reading, high_reading, low_act, high_act = process_score(sat_math, sat_reading, act)

		# Compose inner JSON 
		school_JSON["scores"]["low_sat_math"] = low_math
		school_JSON["scores"]["high_sat_math"] = high_math
		school_JSON["scores"]["low_sat_reading"] = low_reading
		school_JSON["scores"]["high_sat_reading"] = high_reading
		school_JSON["scores"]["low_act"] = low_act
		school_JSON["scores"]["high_act"] = high_act

		# Append to list 
		school_jsons.append(school_JSON)

	with open("../../JSONS/scores.json", "w") as outfile: 
		json.dump(school_jsons, outfile)


get_scores()










