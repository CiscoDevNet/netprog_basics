#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

data_library_exercises.py
Illustrate the following concepts:
- Commands from slides exploring data interactions 
"""

# XML 
print("Treat XML like Python Dictionaries with xmltodict\n\n")
import xmltodict 
from pprint import pprint 

xml_example = open("xml_example.xml").read() 
pprint(xml_example)

xml_dict = xmltodict.parse(xml_example)
int_name = xml_dict["interface"]["name"]
print(int_name)

print(xmltodict.unparse(xml_dict))

print("\n\n")

# JSON 
print("To JSON and back again with json\n\n")
import json 
from pprint import pprint 

json_example = open("json_example.json").read()
pprint(json_example)

json_python = json.loads(json_example)
int_name = json_python["ietf-interfaces:interface"]["name"]
print(int_name)

print(json.dumps(json_python))

print("\n\n")

# YAML 
print("YAML? Yep, Python Can Do That Too!\n\n")
import yaml 
from pprint import pprint 

yml_example = open("yaml_example.yaml").read() 
pprint(yml_example)

# Note: The video used the yaml.load() method. This method 
#  has security vulnerabilities and has been deprecated. The 
#  yaml.safe_load() method is the suggested way to load YAML
#  data now.
# You can read about this at https://msg.pyyaml.org/load
yaml_python = yaml.safe_load(yml_example)
int_name = yaml_python["ietf-interfaces:interface"]["name"]
print(int_name)

print(yaml.dump(yaml_python))

print("\n\n")

# CSV
print("Import Spreadsheets and Data with csv\n\n")
import csv 
from pprint import pprint 

csv_example = open("csv_example.csv").read() 
pprint(csv_example)

csv_example = open("csv_example.csv")
csv_python = csv.reader(csv_example)

for row in csv_python: 
    print("{} is in {} and has IP {}.".format(row[0], row[2], row[1]))

print("\n\n")