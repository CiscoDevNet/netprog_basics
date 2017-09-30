#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Controllers
Lesson: Program your own DNA with APIC-EM APIs
Author: Hank Preston <hapresto@cisco.com>

troubleshoot_full.py
Illustrate the following concepts:
- Automating common information gathering used in troubleshooting
- Replicating "runbook logic" in code
- Leveraging REST APIs in Python
- Using details from one request in the next
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from device_info import apicem
from time import sleep
import json
import requests
import sys
import urllib3

# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
              'content-type': "application/json",
              'x-auth-token': ""
          }


def apic_login(apic, username, password):
    """
    Use the REST API to Log into an APIC-EM and retrieve ticket
    """
    url = "https://{}/api/v1/ticket".format(apic)
    payload = {"username": username, "password": password}

    # Make Login request and return the response body
    response = requests.request("POST", url, data=json.dumps(payload),
                                headers=headers, verify=False)
    return response.json()["response"]


# Entry point for program
if __name__ == '__main__':
    # Setup Arg Parse for Command Line parameters
    import argparse
    parser = argparse.ArgumentParser()

    # Command Line Parameters for Source and Destination IP
    parser.add_argument("source_ip", help = "Source IP Address")
    parser.add_argument("destination_ip", help = "Destination IP Address")
    args = parser.parse_args()

    # Get Source and Destination IPs from Command Line
    source_ip = args.source_ip
    destination_ip = args.destination_ip

    # Print Starting message
    print("Running Troubleshooting Script for ")
    print("      Source IP:      {} ".format(source_ip))
    print("      Destination IP: {}".format(destination_ip))
    print("")

    # Log into the APIC-EM Controller to get Ticket
    login = apic_login(apicem["host"], apicem["username"], apicem["password"])
