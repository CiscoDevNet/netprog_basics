#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Device APIs
Lesson: Getting the YANG of it
Author: Hank Preston <hapresto@cisco.com>

example1.py
Illustrate the following concepts:
- Connect with NETCONF
- Print to screen the <data>
- Used to compare to data model
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from device_info import ios_xe1
from ncclient import manager
import xml.dom.minidom

# NETCONF filter to use
netconf_filter = open("filter-ietf-interfaces.xml").read()


if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        netconf_reply = m.get_config("running", netconf_filter)
        interfaces = xml.dom.minidom.parseString(netconf_reply.xml)
        interfaces = interfaces.getElementsByTagName("interfaces")
        print(interfaces[0].toprettyxml())
