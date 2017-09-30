! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Controllers
Lesson: ACI Programmability Part 2
Author: Hank Preston <hapresto@cisco.com>

toolkit_new_policy.py
Illustrate the following concepts:
- Create Complete Application Policy using ACI Toolkit
- Intended to be entered into an interactive
  interpreter
"""

# Import modules
from device_info import apic
from acitoolkit.acitoolkit import *
from pprint import pprint

# Establish Session Object and Log into APIC
session = Session(apic['host'],
                  apic['username'],
                  apic['password'])
session.login()
session.logged_in()

# Create New Tenant and Main Network Object
my_tenant = Tenant("Hanks_Tenant")
my_tenant.get_json()
my_vrf = Context("Hanks_VRF", my_tenant)
my_bd = BridgeDomain("Hanks_BD", my_tenant)
my_tenant.get_json()
pprint(my_tenant.get_json())

# Configure Bridge Domain Properties
my_bd.add_context(my_vrf)
my_subnet = Subnet("Hanks_Subnet", my_bd)
my_subnet.set_scope("public")
my_subnet.set_addr("10.10.10.1/24")

# Create Application Profile and EPGs
my_app = AppProfile("Hanks_App", my_tenant)
my_epg = EPG("Hanks_EPG", my_app)
my_epg.add_bd(my_bd)

# Create Security Policy Elements
# Create new Filter
filter_web = Filter("web", my_tenant)

FilterEntry("tcp-80", filter_web,
              etherT="ip", prot="tcp",
              dFromPort="http", dToPort="http")

FilterEntry("tcp-443", filter_web,
             etherT="ip", prot="tcp",
             dFromPort="https", dToPort="https")

# Create New Contract
contract_web = Contract("web", my_tenant)
contract_subject_web= ContractSubject("web", contract_web)

# Add Filter to Contract
contract_subject_web.add_filter(filter_web)

# Add Contract to EPG
my_epg.provide(contract_web)

# Review the ACI Object Definition created
pprint(my_tenant.get_json())

# Push configuration to APIC
response =  session.push_to_apic(
                     my_tenant.get_url(),
                     data=my_tenant.get_json()
                )

# View Status
response.status_code
response.reason

# Check in APIC GUI

# Delete Tenant
my_tenant.mark_as_deleted()
pprint(my_tenant.get_json())

response =  session.push_to_apic(
                     my_tenant.get_url(),
                     data=my_tenant.get_json()
                )

# Check in APIC GUI
