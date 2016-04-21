#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json
import sys

# Get all the links to pages of states with schools that would be appropriate given an SAT score 
def req_state_links(score): 
	url = "http://www.collegesimply.com/guides/" + str(score) + "-on-the-sat/?view=all"

	page = r.get(url)
	tree = html.fromstring(page.content)
	states = tree.xpath("//td/h5/span/a")
	
	state_links = [] 

	for s in states: 
		state_links.append(s.attrib["href"])

	return state_links


# Obtain the school links from a given list of state links for a specific SAT score 
def req_school_links(state_links): 
	url = "http://www.collegesimply.com"
	for link in state_links: 
		page = r.get(url + link)
		tree = html.fromstring(page.content)
		schools = tree.xpath("//tr/td/a")

		school_links = [] 

		for s in schools: 
			school_links.append(s.attrib["href"])

	return school_links


