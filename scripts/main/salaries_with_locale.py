#!/usr/bin/env python 

from lxml import html
import requests as r
import re # Regular expressions
import json
import sys


def get_lat_long(api_key, zip_code):

  geocode = r.get("https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:" + zip_code + "&key=" + api_key)
  location_json = geocode.json()["results"][0]["geometry"]["location"]
  lat = location_json["lat"]
  lng = location_json["lng"]

  return (lat, lng)



def add_locales_to_salaries(api_key):
  # Obtain the curated_salaries.json + corresponding JSON
  with open('../../JSONS/curated_salaries.json') as salary_JSON:
    salary_json = json.load(salary_JSON)

  result_list = []
  for i in salary_json:
    element = i.copy()
    # Get geographic info (lat/long)
    zip_code = element["salary_info"]["zip_code"]

    # Manually check for Cornell zipcode (b/c it's incorrect)
    zip_code = "14850" if (zip_code == "14853") else zip_code
    print zip_code

    lat, lng = get_lat_long(api_key, zip_code)

    # lat/long JSON addition
    location_JSON = { "location_info": { "lat": lat, "lng": lng } }
    element.update(location_JSON)

    result_list.append(element)

  # dump final_json to file
  with open("../../salary_schools.json", "w") as outfile:
    json.dump(result_list, outfile)


add_locales_to_salaries(sys.argv[1])
