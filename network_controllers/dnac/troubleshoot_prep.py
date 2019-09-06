#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Controllers
Lesson: Cisco DNA Center Platform APIs Part 2: Network Troubleshooting
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

from device_info import dnac as dnac
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


def dnac_login(dnac, port, username, password):
    """
    Use the REST API to Log into an DNA Center and retrieve ticket
    """
    url = "https://{}:{}/dna/system/api/v1/auth/token".format(dnac, port)

    # Make Login request and return the response body
    response = requests.request("POST", url,
                                auth = (username, password),
                                headers=headers, verify=False)
    return response.json()["Token"]


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

    # Log into the dnac Controller to get Ticket
    token = dnac_login(dnac["host"], dnac["port"], dnac["username"], dnac["password"])
