#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json

def get_admissions():
	page = r.get("http://www.collegesimply.com/guides/low-acceptance-rate/?view=all")
	tree = html.fromstring(page.content)

	schools = tree.xpath('//tbody/tr/td/a/text()')
	#for s in schools: 
		#print s

	schools_infos = tree.xpath('//tbody/tr/td/span/text()')

	#for i in schools_infos: 
		#print i 

	rates = tree.xpath('//tbody/tr/td/text()')
	new_rates = []
	for l in rates: # Curate the scraped info 
		if not ("\n" in l) and not ("%" not in l): 
			new_rates.append(l)
	print new_rates



get_admissions() 