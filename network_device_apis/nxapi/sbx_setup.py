#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Device APIs
Lesson: NX-API Part 2
Author: Hank Preston <hapresto@cisco.com>

sbx_setup.py
Deploy baseline configuration for the lesson:
- Add 3 VLANs to the Switch Configuration
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import requests
import json

# Switch Connection Info
url = 'https://10.10.20.58/ins'
switchuser = 'admin'
switchpassword = 'cisco123'
myheaders = {'content-type': 'application/json'}

# Configuration Payload
payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "vlan 101 ;name Web_VLAN ;vlan 102 ;name App_VLAN ;vlan 103 ;name Data_VLAN", # noqa
    "output_format": "json"
  }
}

# Send Configuration
response = requests.post(
                          url,
                          data=json.dumps(payload),
                          headers=myheaders,
                          auth=(switchuser, switchpassword),
                          verify=False
                         ).json()
