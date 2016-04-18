#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json

def get_salaries(): 
	school_jsons = [] 	
	for i in range(1, 2): # Range of 1 to 69 pages of schools; should go to 70, but testing on this first 
		page = r.get("http://www.payscale.com/college-salary-report/bachelors?page=" + str(i))
		print page.content # This prints the HTML, which includes a massive school json 


get_salaries() 


