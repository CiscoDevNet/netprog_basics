#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Controllers
Lesson: Program your own DNA with DNA Center APIs
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

from device_info import dnac
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


def host_list(dnac, ticket, ip=None, mac=None, name=None):
    """
    Use the REST API to retrieve the list of hosts.
    Optional parameters to filter by:
      IP address
      MAC address
      Hostname
    """
    url = "https://{}/api/v1/host".format(dnac)
    headers["x-auth-token"] = ticket
    filters = []

    # Add filters if provided
    if ip:
        filters.append("hostIp={}".format(ip))
    if mac:
        filters.append("hostMac={}".format(mac))
    if name:
        filters.append("hostName={}".format(name))
    if len(filters) > 0:
        url += "?" + "&".join(filters)

    # Make API request and return the response body
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]


def verify_single_host(host, ip):
    """
    Simple function to verify only a single host returned from query.
    If no hosts, or multiple hosts are returned, an error message is printed
    and the program exits.
    """
    if len(host) == 0:
        print("Error: No host with IP address {} was found".format(ip))
        sys.exit(1)
    if len(host) > 1:
        print("Error: Multiple hosts with IP address {} were found".format(ip))
        print(json.dumps(host, indent=2))
        sys.exit(1)


def print_host_details(host):
    """
    Print to screen interesting details about a given host.
    Input Paramters are:
      host_desc: string to describe this host.  Example "Source"
      host: dictionary object of a host returned from DNA Center
    Standard Output Details:
      Host Name (hostName) - If available
      Host IP (hostIp)
      Host MAC (hostMac)
      Network Type (hostType) - wired/wireless
      Host Sub Type (subType)
      VLAN (vlanId)
      Connected Network Device (connectedNetworkDeviceIpAddress)

    Wired Host Details:
      Connected Interface Name (connectedInterfaceName)

    Wireless Host Details:
      Connected AP Name (connectedAPName)
    """
    # If optional host details missing, add as "Unavailable"
    if "hostName" not in host.keys():
        host["hostName"] = "Unavailable"

    # Print Standard Details
    print("Host Name: {}".format(host["hostName"]))
    print("Network Type: {}".format(host["hostType"]))
    print("Connected Network Device: {}".format(host["connectedNetworkDeviceIpAddress"]))  # noqa: E501

    # Print Wired/Wireless Details
    if host["hostType"] == "wired":
        print("Connected Interface Name: {}".format(host["connectedInterfaceName"]))  # noqa: E501
    if host["hostType"] == "wireless":
        print("Connected AP Name: {}".format(host["connectedAPName"]))

    # Print More Standard Details
    print("VLAN: {}".format(host["vlanId"]))
    print("Host IP: {}".format(host["hostIp"]))
    print("Host MAC: {}".format(host["hostMac"]))
    print("Host Sub Type: {}".format(host["subType"]))

    # Blank line at the end
    print("")


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

    # Log into the DNA Center Controller to get Ticket
    token = dnac_login(dnac["host"], dnac["username"], dnac["password"])

    # Step 1: Identify involved hosts
    # Retrieve Host Details from DNA Center
    source_host = host_list(dnac["host"], token,
                            ip=source_ip)
    destination_host = host_list(dnac["host"], token,
                                 ip=destination_ip)

    # Verify single host found for each IP
    verify_single_host(source_host, source_ip)
    verify_single_host(destination_host, destination_ip)

    # Print Out Host details
    print("Source Host Details:")
    print("-" * 25)
    print_host_details(source_host[0])

    print("Destination Host Details:")
    print("-" * 25)
    print_host_details(destination_host[0])
