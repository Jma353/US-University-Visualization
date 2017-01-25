#!/usr/bin/env python 

from lxml import html
import requests as r
import re # Regular expressions
import json

def get_admissions():
  page = r.get("http://www.collegesimply.com/guides/low-acceptance-rate/?view=all")
  tree = html.fromstring(page.content)

  # Obtain data
  schools = tree.xpath('//tbody/tr/td/a/text()')
  schools_infos = tree.xpath('//tbody/tr/td/span/text()')
  rates = tree.xpath('//tbody/tr/td/text()')

  # Modify rates as necessary
  new_rates = []
  for l in rates: # Curate the scraped info
    if not ("\n" in l) and not ("%" not in l):
      new_rates.append(l)


  school_jsons = []

  for i in range(len(schools)): # For i w/in the indexed range of the schools
    school_JSON = {}
    school_JSON["school"] = schools[i]
    school_JSON["admission_info"] = {}
    school_JSON["admission_info"]["acceptance_rate"] = int(re.sub("%", "", new_rates[i]))
    school_JSON["admission_info"]["location"] = schools_infos[i*3]
    school_JSON["admission_info"]["applicants"] = int(re.sub(",", "", schools_infos[i*3+1].split(" ")[0]))
    school_JSON["admission_info"]["difficulty"] = schools_infos[i*3+2]

    school_jsons.append(school_JSON)

  with open('admissions.json', 'w+') as outfile:
    json.dump(school_jsons, outfile)


get_admissions()
