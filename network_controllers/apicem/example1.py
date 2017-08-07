#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Controllers
Lesson: Program your own DNA with APIC-EM APIs
Author: Hank Preston <hapresto@cisco.com>

example1.py
Illustrate the following concepts:
- Building APIC-EM API Code
- Start from Postman Auto-generated code
- Multiple requests in one script
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from device_info import apicem
import requests
import json

headers = {
              'content-type': "application/json",
              'x-auth-token': ""
          }

def apic_login(host, username, password):
    """
    Use the REST API to Log into an APIC-EM and retrieve ticket
    """
    url = "https://{}/api/v1/ticket".format(host)
    payload = {"username": username, "password": password}

    # Make Login request and return the response body
    response = requests.request("POST", url, data=json.dumps(payload),
                                headers=headers, verify=False)
    return response.json()["response"]


def network_device_list(host, ticket):
    """
    Use the REST API to retrieve the list of network devices
    """
    url = "https://{}/api/v1/network-device".format(host)
    headers["x-auth-token"] = ticket
    
    # Make API request and return the response body
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]


# Entry point for program
if __name__ == '__main__':
    # Log into the APIC-EM Controller to get Ticket
    login = apic_login(apicem["host"], apicem["username"], apicem["password"])

    # Get the list of devices
    devices = network_device_list(apicem["host"], login["serviceTicket"])

    # Loop through the devices and print details
    for device in devices:
        print("{} in family {}".format(device["hostname"], device["family"]))
        print("  Management IP: {}".format(device["managementIpAddress"]))
        print("  Platform Type: {}".format(device["platformId"]))
        print("  Software Version: {}".format(device["softwareVersion"]))
        print("")
