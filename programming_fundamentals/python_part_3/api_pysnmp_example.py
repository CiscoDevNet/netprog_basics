#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_snmp_example.py
Illustrate the following concepts:
- How to make an SNMP GET with PySNMP 
- Intended to be entered into an interactive
  interpreter

Sandbox Usage: The DevNet Always On IOS XE Sandbox does NOT
have SNMP available.  If you'd like to try this example, you 
can reserve the "IOS XE on CSR Recommended Code" Sandbox
"""

from pysnmp.hlapi import *
from pprint import pprint

router = {"ip": "10.10.20.48",
          "port": 161,
          "user": "developer",
          "pass": "C1sco12345"}

iterator = getCmd(SnmpEngine(),
                  CommunityData('public'),
                  UdpTransportTarget((router["ip"], router["port"])),
                  ContextData(),
                  ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:  # SNMP engine errors
    print(errorIndication)
else:
    if errorStatus:  # SNMP agent errors
        print('%s at %s' % (errorStatus.prettyPrint(),
                            varBinds[int(errorIndex)-1] if errorIndex else '?'))
    else:
        for varBind in varBinds:  # SNMP response contents
            print(' = '.join([x.prettyPrint() for x in varBind]))
