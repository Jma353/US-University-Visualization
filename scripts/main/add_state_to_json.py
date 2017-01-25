#!/usr/bin/env python 

from lxml import html
import requests as r
import re # Regular expressions
import json
import sys



with open("overall.json") as uni_JSON:
  uni_info = json.load(uni_JSON)



def find_state(api_key, zip_code):

  geocode = r.get("https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:" + zip_code + "&key=" + api_key)
  location_array = geocode.json()["results"][0]["address_components"]
  location_json = location_array[len(location_array)-2]
  return location_json["long_name"]


def add_states(api_key, uni_info):
  new_list = []
  for uni in uni_info:
    a = uni.copy()
    a["location_info"]["state"] = find_state(api_key, a["salary_info"]["zip_code"])
    new_list.append(a)

  with open("overall_with_state.json", "w") as outfile:
    json.dump(new_list, outfile)


add_states(sys.argv[1], uni_info)
