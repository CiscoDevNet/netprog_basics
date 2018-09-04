#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Controllers
Lesson: Program your own DNA with DNA Center APIs
Author: Hank Preston <hapresto@cisco.com>

example1.py
Illustrate the following concepts:
- Building DNA Center API Code
- Start from Postman Auto-generated code
- Multiple requests in one script
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from device_info import dnac
import requests
import json

headers = {
              'content-type': "application/json",
              'x-auth-token': ""
          }

def dnac_login(host, username, password):
    """
    Use the REST API to Log into an DNA Center and retrieve ticket
    """
    url = "https://{}/api/system/v1/auth/token".format(host)

    # Make Login request and return the response body
    response = requests.request("POST", url,
                                auth = (username, password),
                                headers=headers, verify=False)
    return response.json()["Token"]


def network_device_list(host, token):
    """
    Use the REST API to retrieve the list of network devices
    """
    url = "https://{}/api/v1/network-device".format(host)
    headers["x-auth-token"] = token

    # Make API request and return the response body
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]


# Entry point for program
if __name__ == '__main__':
    # Log into the DNA Center Controller to get Ticket
    token = dnac_login(dnac["host"], dnac["username"], dnac["password"])

    # Get the list of devices
    devices = network_device_list(dnac["host"], token)

    # Loop through the devices and print details
    for device in devices:
        print("{} in family {}".format(device["hostname"], device["family"]))
        print("  Management IP: {}".format(device["managementIpAddress"]))
        print("  Platform Type: {}".format(device["platformId"]))
        print("  Software Version: {}".format(device["softwareVersion"]))
        print("")
