#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_requests_example.py
Illustrate the following concepts:
- Making REST API calls using requests library
- Intended to be entered into an interactive
  interpreter
"""


import requests
from pprint import pprint
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

router = {"ip": "ios-xe-mgmt.cisco.com",
	      "port": "443",
          "user": "developer",
          "pass": "lastorangerestoreball8876"}

headers = {"Accept": "application/yang-data+json"}

u = "https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet1"

u = u.format(router["ip"], router["port"])

r = requests.get(u,
		     headers = headers,
		     auth=(router["user"], router["pass"]),
		     verify=False)

pprint(r.text)

api_data = r.json()
interface_name = api_data["Cisco-IOS-XE-interfaces-oper:interface"]["name"]
interface_name
