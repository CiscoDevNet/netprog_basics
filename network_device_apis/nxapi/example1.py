#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Device APIs
Lesson: NX-API Part 1
Author: Hank Preston <hapresto@cisco.com>

example1.py
Illustrate the following concepts:
- NX-API CLI code generation from Developer Sandbox
- INS-API JSON
- Execute command, print output
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import requests
import json

"""
Modify these please
"""
url='http://10.10.20.58/ins'
switchuser='admin'
switchpassword='cisco123'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show vlan bri",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

# Extract interesting info from Response
vlan_list = response["ins_api"]["outputs"]["output"]["body"]["TABLE_vlanbriefxbrief"]["ROW_vlanbriefxbrief"]

# Print out the vlan details
for vlan in vlan_list:
    print("VLAN Name: {}".format(vlan["vlanshowbr-vlanname"]))
