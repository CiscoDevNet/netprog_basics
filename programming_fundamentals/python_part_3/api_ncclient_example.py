#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_ncclient_example.py
Illustrate the following concepts:
- Making NETCONF calls using ncclient library
- Intended to be entered into an interactive
  interpreter
"""

from ncclient import manager
from pprint import pprint
import xmltodict

router = {"ip": "10.10.20.48",
          "port": 830,
          "user": "cisco",
          "pass": "cisco_1234!"}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""

m = manager.connect(host=router["ip"],
                    port=router["port"],
                    username=router["user"],
                    password=router["pass"],
                    hostkey_verify=False)

interface_netconf = m.get_config("running", netconf_filter)
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(interface_python["interfaces"]["interface"]["name"]["#text"])
