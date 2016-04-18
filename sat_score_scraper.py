#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json

def get_scores(): 
	page = r.get("https://www.powerscore.com/sat/help/average_test_scores.cfm")
	tree = html.fromstring(page.content)
	schools = tree.xpath('//table[@id="collegestats"]/tbody/tr/td/b/text()')
	stats = tree.xpath('//table[@id="collegestats"]/tbody/tr/td/text()')
	schools.remove('\r\n   ') # Remove the stray empty value from the scrape 
	school_jsons = []
	for i in range(len(schools)):
		school_JSON = {} 
		school_JSON["school"] = re.sub(' +', ' ', schools[i]) # Clean up extraneous spaces 
		school_JSON["scores"] = {}
		school_JSON["scores"]["sat_math"] = stats[i*3]
		school_JSON["scores"]["sat_reading"] = stats[i*3+1]
		school_JSON["scores"]["act"] = stats[i*3+2] 
		school_jsons.append(school_JSON)

	print school_jsons

get_scores()




