#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json

# DON'T COMMIT THIS 
api_key = "AIzaSyCnkX05akk5jUcpy13lasHXzcnAzISyjHY"


def geocode_test(api_key): 

	geocode = r.get("https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:3755&key=" + api_key)
	print geocode.json() # ["results"][0]["geometry"]["location"] 



geocode_test(api_key)
