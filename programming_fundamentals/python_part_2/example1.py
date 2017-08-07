#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 2
Author: Hank Preston <hapresto@cisco.com>

example1.py
Illustrate the following concepts:
- importing and using libraries
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

# Import data from another script
from common_vars import shapes
# Import a library that offers date-time capabilities
import datetime

print("The shapes are:")
for shape in shapes:
    print(shape)
print("")

# Get Current Date and Time
date_now = datetime.datetime.now()
print("It is currently {}.".format(str(date_now)))

# Add 1000 minutes to Current Date and Time
new_date = date_now + datetime.timedelta(minutes=1000)
print("In 1000 minutes it will be {}.".format(str(new_date)))
