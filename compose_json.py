#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json

with open('scores.json') as score_json: 
	json_data = json.load(score_json)
	print json_data 

