#!/usr/bin/env python 

from lxml import html 
import requests as r 
import re # Regular expressions 
import json
import sys


def find_state(api_key, zip_code):

	geocode = r.get("https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:" + zip_code + "&key=" + api_key)
	location_array = geocode.json()["results"][0]["address_components"]
	location_json = location_array[len(location_array)-2]
	return location_json["long_name"]

print find_state(sys.argv[1], "94305")









