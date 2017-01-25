#!/usr/bin/env python 

from lxml import html
import requests as r
import re # Regular expressions
import json
import sys


# Load the current JSON we're working with
with open("../../JSONS/salary_schools.json") as school_JSON:
  curr_schools = json.load(school_JSON)


# Simple function to compare similar names
def similar_names(name1, name2):

  name1_array = name1.split(" ")
  name2_array = name2.split(" ")
  length = max(len(name1_array), len(name2_array))
  sim_count = 0
  for i in name1_array:
    for j in name2_array:
      if i.lower() == j.lower():
        sim_count += 1

  # for higher quality intersection of datasets
  # this is ugly, but pressed for time
  if ("university of" in name1.lower()) or ("university of" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("state" in name1.lower()) or ("state" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("wesleyan university" in name1.lower()) or ("wesleyan university" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("college of" in name1.lower()) or ("college of" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("institute of" in name1.lower()) or ("institute of" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("maritime" in name1.lower()) or ("maritime" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("tech" in name1.lower()) or ("tech" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("technological" in name1.lower()) or ("technological" in name2.lower()):
    return float(sim_count)/length >= 0.85
  elif ("saint" in name1.lower()) or ("saint" in name2.lower()):
    return float(sim_count)/length >= 0.85
  else:
    return float(sim_count)/length >= 0.70


# Helper function to check listings of schools
def in_list(name, the_list):
  for i in range(len(the_list)):
    if similar_names(name, the_list[i]["school"]):
      return [True, i]
  return [False, None]


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
def req_school_links(state_links, curr_schools):
  url = "http://www.collegesimply.com"
  school_links = []
  school_indices = []
  for link in state_links:
    page = r.get(url + link)
    tree = html.fromstring(page.content)
    schools = tree.xpath("//tr/td/a")
    school_names = tree.xpath("//tr/td/a/text()")
    for i in range(len(schools)):
      check = in_list(school_names[i], curr_schools)
      if check[0]:
        school_links.append(schools[i].attrib["href"])
        school_indices.append(check[1])
  return school_links, school_indices


# Compose the school JSON list (while also combining with the curr_schools JSONs that matched)
def req_school_json(school_links, school_indices, curr_schools):
  url = "http://www.collegesimply.com"
  overallJSON = []
  for j in range(len(school_links)):
    page = r.get(url + school_links[j])
    tree = html.fromstring(page.content)
    school_info = tree.xpath("//tbody/tr/td/text()")

    school_json = {"link": school_links[j], "admissions_info": {}, "score_info": {} }
    print school_json["link"]
    if "SAT Reading" in page.content:
      for i in range(len(school_info)):
        if i == 3:
          school_json["admissions_info"]["applied"] = int(re.sub(",", "", school_info[i]))
        elif i == 11:
          school_json["admissions_info"]["acceptance_rate"] = int(re.sub("%", "", school_info[i]))
        elif school_info[i] == "SAT Reading":
          school_json["score_info"]["sat_reading_low"] = "N/A" if (school_info[i+1] == "N/A") else int(school_info[i+1])
          school_json["score_info"]["sat_reading_high"] = "N/A" if (school_info[i+2] == "N/A") else int(school_info[i+2])
          school_json["score_info"]["sat_math_low"] = "N/A" if (school_info[i+4] == "N/A") else int(school_info[i+4])
          school_json["score_info"]["sat_math_high"] = "N/A" if (school_info[i+5] == "N/A") else int(school_info[i+5])

    other_json = curr_schools[school_indices[j]].copy()
    other_json.update(school_json)
    print other_json
    overallJSON.append(other_json)

  return overallJSON


# Over all function to compose JSON
def overall(curr_schools):
  state_links = req_state_links(1600)
  school_links, school_indices = req_school_links(state_links, curr_schools)
  FINAL_JSON = req_school_json(school_links, school_indices, curr_schools)

  with open("overall.json", "w") as outfile:
    json.dump(FINAL_JSON, outfile)



overall(curr_schools)
