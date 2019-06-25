#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Controllers
Lesson: ACI Programmability Part 2
Author: Hank Preston <hapresto@cisco.com>

toolkit_getting_started.py
Illustrate the following concepts:
- Import ACI Toolkit library
- Connect to APIC Controller
- Print list of tenants
- Intended to be entered into an interactive
  interpreter
"""

from device_info import apic
from acitoolkit.acitoolkit import Session, Tenant

session = Session(apic['host'],
                  apic['username'],
                  apic['password'])
session.login()
session.logged_in()

tenants = Tenant.get(session)

for tenant in tenants:
    print(tenant.name)
    if tenant.name == "Heroes":
        heroe_tenant = tenant
