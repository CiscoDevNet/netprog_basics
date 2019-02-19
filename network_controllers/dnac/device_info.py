#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Author: Hank Preston <hapresto@cisco.com>

device_info.py
Illustrate the following concepts:
- Store device info for Sandbox Infrastructure used
  in examples
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

# DevNet Always-On NETCONF/YANG & RESTCONF Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
ios_xe1 = {
             "address": "ios-xe-mgmt.cisco.com",
             "port": 10000,
             "username": "root",
             "password": "D_Vay!_10&"
          }

# DevNet IOS XE Programmability Sandbox Device
# https://devnetsandbox.cisco.com/RM/Diagram/Index/7fd27b24-7034-477d-9ad2-e2c8096dd1a5?diagramType=Topology
ios_xe2 = {
             "address": "10.10.20.21",
             "port": 830,
             "username": "root",
             "password": "cisco123"
          }


# DevNet Always-On Sandbox APIC-EM
# https://devnetsandbox.cisco.com/RM/Diagram/Index/2e0f9525-5f46-4f46-973e-0f0c1bf934fa?diagramType=Topology
apicem = {
             "host": "sandboxapicem.cisco.com",
             "username": "devnetuser",
             "password": "Cisco123!",
             "port": 443
         }

# DevNet Always-On Sandbox ACI APIC
# https://devnetsandbox.cisco.com/RM/Diagram/Index/5a229a7c-95d5-4cfd-a651-5ee9bc1b30e2?diagramType=Topology
apic = {
             "host": "https://sandboxapicdc.cisco.com",
             "username": "admin",
             "password": "ciscopsdt",
             "port": 443
         }

# DevNet Always-On Sandbox DNA Center
# https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology
dnac = {
             "host": "sandboxdnac.cisco.com",
             "username": "devnetuser",
             "password": "Cisco123!",
             "port": 443
         }
