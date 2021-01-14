#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_netmiko_example.py
Illustrate the following concepts:
- Making CLI calls using netmiko library
- Intended to be entered into an interactive
  interpreter
"""

from netmiko import ConnectHandler
from pprint import pprint

router = {"device_type": "cisco_ios",
          "host": "ios-xe-mgmt.cisco.com",
          "port": 8181,
          "user": "developer",
          "pass": "C1sco12345"}

net_connect = ConnectHandler(ip=router["host"],
                             port=router["port"], 
                             username=router["user"],
                             password=router["pass"],
                             device_type=router["device_type"])

interface_cli = net_connect.send_command("show run int Gig1")

pprint(interface_cli)
