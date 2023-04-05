#!/usr/bin/env python3
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

# # IOS XE on CSR Recommended Code AlwaysOn
# # https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
ios_xe1 = {
             "address": "sandbox-iosxe-recomm-1",
             "port": 830,
             "username": "developer",
             "password": "C1sco12345"
          }

# DevNet Always-On Sandbox ACI APIC
# https://devnetsandbox.cisco.com/RM/Diagram/Index/18a514e8-21d4-4c29-96b2-e3c16b1ee62e?diagramType=Topology
apic = {
             "host": "https://sandboxapicdc.cisco.com",
             "username": "admin",
             "password": "!v3G@!4@Y",
             "port": 443
         }

