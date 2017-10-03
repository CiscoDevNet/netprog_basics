#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Application Hosting
Lesson: Package, Deploy and Run Applications in the Network with IOx
Author: Hank Preston <hapresto@cisco.com>

main.py
Illustrate the following concepts:
- Deploy an IOx application using Docker tooling
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from bottle import route, run
from datetime import datetime

@route('/status/<device_id>')
def status(device_id):
   return { "system": 1, "device": str(device_id) }

@route('/time')
def time():
   current_time = datetime.now().isoformat(' ')
   return {"system": 1, "datetime": current_time}

run(host='0.0.0.0', port=8000)
