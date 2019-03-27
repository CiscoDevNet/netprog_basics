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
      host: dictionary object of a host returned from dnac
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


def network_device_list(dnac, ticket, id=None):
    """
    Use the REST API to retrieve the list of network devices.
    If a device id is provided, return only that device
    """
    url = "https://{}/dna/intent/api/v1/network-device".format(dnac)
    headers["x-auth-token"] = ticket

    # Change URL to single device given an id
    if id:
        url += "/{}".format(id)

    # Make API request and return the response body
    response = requests.request("GET", url, headers=headers, verify=False)

    # Always return a list object, even if single device for consistency
    if id:
        return [response.json()["response"]]

    return response.json()["response"]


def interface_details(dnac, ticket, id):
    """
    Use the REST API to retrieve details about an interface based on id.
    """
    url = "https://{}/dna/intent/api/v1/interface/{}".format(dnac, id)
    headers["x-auth-token"] = ticket

    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]


def print_network_device_details(network_device):
    """
    Print to screen interesting details about a network device.
    Input Paramters are:
      network_device: dict object of a network device returned from dnac
    Standard Output Details:
      Device Hostname (hostname)
      Management IP (managementIpAddress)
      Device Location (locationName)
      Device Type (type)
      Platform Id (platformId)
      Device Role (role)
      Serial Number (serialNumber)
      Software Version (softwareVersion)
      Up Time (upTime)
      Reachability Status (reachabilityStatus)
      Error Code (errorCode)
      Error Description (errorDescription)
    """

    # Print Standard Details
    print("Device Hostname: {}".format(network_device["hostname"]))
    print("Management IP: {}".format(network_device["managementIpAddress"]))
    print("Device Location: {}".format(network_device["locationName"]))
    print("Device Type: {}".format(network_device["type"]))
    print("Platform Id: {}".format(network_device["platformId"]))
    print("Device Role: {}".format(network_device["role"]))
    print("Serial Number: {}".format(network_device["serialNumber"]))
    print("Software Version: {}".format(network_device["softwareVersion"]))
    print("Up Time: {}".format(network_device["upTime"]))
    print("Reachability Status: {}".format(network_device["reachabilityStatus"]))  # noqa: E501
    print("Error Code: {}".format(network_device["errorCode"]))
    print("Error Description: {}".format(network_device["errorDescription"]))

    # Blank line at the end
    print("")


def print_interface_details(interface):
    """
    Print to screen interesting details about an interface.
    Input Paramters are:
      interface: dictionary object of an interface returned from dnac
    Standard Output Details:
      Port Name - (portName)
      Interface Type (interfaceType) - Physical/Virtual
      Admin Status - (adminStatus)
      Operational Status (status)
      Media Type - (mediaType)
      Speed - (speed)
      Duplex Setting (duplex)
      Port Mode (portMode) - access/trunk/routed
      Interface VLAN - (vlanId)
      Voice VLAN - (voiceVlan)
    """

    # Print Standard Details
    print("Port Name: {}".format(interface["portName"]))
    print("Interface Type: {}".format(interface["interfaceType"]))
    print("Admin Status: {}".format(interface["adminStatus"]))
    print("Operational Status: {}".format(interface["status"]))
    print("Media Type: {}".format(interface["mediaType"]))
    print("Speed: {}".format(interface["speed"]))
    print("Duplex Setting: {}".format(interface["duplex"]))
    print("Port Mode: {}".format(interface["portMode"]))
    print("Interface VLAN: {}".format(interface["vlanId"]))
    print("Voice VLAN: {}".format(interface["voiceVlan"]))

    # Blank line at the end
    print("")


def run_flow_analysis(dnac, ticket, source_ip, destination_ip):
    """
    Use the REST API to initiate a Flow Analysis (Path Trace) from a given
    source_ip to destination_ip.  Function will wait for analysis to complete,
    and return the results.
    """
    base_url = "https://{}/dna/intent/api/v1/flow-analysis".format(dnac)
    headers["x-auth-token"] = ticket

    # initiate flow analysis
    body = {"destIP": destination_ip, "sourceIP": source_ip}
    initiate_response = requests.post(base_url, headers=headers, verify=False,
                                      json=body)

    # Verify successfully initiated.  If not error and exit
    if initiate_response.status_code != 202:
        print("Error: Flow Analysis Initiation Failed")
        print(initiate_response.text)
        sys.exit(1)

    # Check status of analysis and wait until completed
    flowAnalysisId = initiate_response.json()["response"]["flowAnalysisId"]
    detail_url = base_url + "/{}".format(flowAnalysisId)
    detail_response = requests.get(detail_url, headers=headers, verify=False)
    while not detail_response.json()["response"]["request"]["status"] == "COMPLETED":  # noqa: E501
        print("Flow analysis not complete yet, waiting 5 seconds")
        sleep(5)
        detail_response = requests.get(detail_url, headers=headers,
                                       verify=False)

    # Return the flow analysis details
    return detail_response.json()["response"]


def print_flow_analysis_details(flow_analysis):
    """
    Print to screen interesting details about the flow analysis.
    Input Parameters are:
      flow_analysis: dictionary object of a flow analysis returned from dnac
    """
    hops = flow_analysis["networkElementsInfo"]

    print("Number of Hops from Source to Destination: {}".format(len(hops)))
    print()

    # Print Details per hop
    print("Flow Details: ")
    # Hop 1 (index 0) and the last hop (index len - 1) represent the endpoints
    for i, hop in enumerate(hops):
        if i == 0 or i == len(hops) - 1:
            continue

        print("*" * 40)
        print("Hop {}: Network Device {}".format(i, hop["name"]))
        # If the hop is "UNKNOWN" continue along
        if hop["name"] == "UNKNOWN":
            print()
            continue

        print("Device IP: {}".format(hop["ip"]))
        print("Device Role: {}".format(hop["role"]))

        # If type is an Access Point, skip interface details
        if hop["type"] == "Unified AP":
            continue
        print()

        # Step 4: Are there any problems along the path?
        # Print details about each interface
        print("Ingress Interface")
        print("-" * 20)
        ingress = interface_details(dnac["host"], token,
                                    hop["ingressInterface"]["physicalInterface"]["id"])  # noqa: E501
        print_interface_details(ingress)
        print("Egress Interface")
        print("-" * 20)
        egress = interface_details(dnac["host"], token,
                                   hop["egressInterface"]["physicalInterface"]["id"])  # noqa: E501
        print_interface_details(egress)

    # Print blank line at end
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

    # Log into the dnac Controller to get Ticket
    token = dnac_login(dnac["host"], dnac["port"], dnac["username"], dnac["password"])

    # Step 1: Identify involved hosts
    # Retrieve Host Details from dnac
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

    # Step 2: Where are they in the network?
    # Retrieve and Print Source Device Details from dnac
    source_host_net_device = network_device_list(dnac["host"],
                                                 token,
                                                 id=source_host[0]["connectedNetworkDeviceId"])  # noqa: E501
    print("Source Host Network Connection Details:")
    print("-" * 45)
    print_network_device_details(source_host_net_device[0])
    # If Host is wired, collect interface details
    if source_host[0]["hostType"] == "wired":
        source_host_interface = interface_details(dnac["host"],
                                                  token,
                                                  id=source_host[0]["connectedInterfaceId"])  # noqa: E501
        print("Attached Interface:")
        print("-" * 20)
        print_interface_details(source_host_interface)

    destination_host_net_device = network_device_list(dnac["host"],
                                                      token,
                                                      id=destination_host[0]["connectedNetworkDeviceId"])  # noqa: E501
    print("Destination Host Network Connection Details:")
    print("-" * 45)
    print_network_device_details(destination_host_net_device[0])
    # If Host is wired, collect interface details
    if destination_host[0]["hostType"] == "wired":
        destination_host_interface = interface_details(dnac["host"],
                                                       token,
                                                       id=destination_host[0]["connectedInterfaceId"])  # noqa: E501
        print("Attached Interface:")
        print("-" * 20)
        print_interface_details(destination_host_interface)

    # Step 3: What path does the traffic take?
    # Step 4: Are there any problems along the path?
    # Run a Flow Analysis for Source/Destionation
    print("Running Flow Analysis from {} to {}".format(source_ip, destination_ip))  # noqa: E501
    print("-" * 55)
    flow_analysis = run_flow_analysis(dnac["host"], token,
                                      source_ip,
                                      destination_ip)

    # Print Out Details
    print_flow_analysis_details(flow_analysis)
