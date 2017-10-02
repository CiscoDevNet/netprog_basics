#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Application Hosting
Lesson: Python at the Edge
Author: Hank Preston <hapresto@cisco.com>

eem_intf_up.py
Illustrate the following concepts:
- Run a Python script due to EEM event
- Leverage the Python API library "cli"
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from cli import configurep
import argparse

# Retrieve the interface from command line using argparse
parser = argparse.ArgumentParser()
parser.add_argument("interface", help="Interface to bring up")
args = parser.parse_args()

# List of commands to run
commands = [
            "interface {}".format(args.interface),
            "no shut"
           ]

# Run commands using Python API
# Commands need to be semicolon seperated
configurep(commands)
