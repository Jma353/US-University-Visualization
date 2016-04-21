#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json
import sys


def geocode_test(): 

	school = r.get("https://bigfuture.collegeboard.org/college-university-search/cornell-university")
	print school.content 


geocode_test()

