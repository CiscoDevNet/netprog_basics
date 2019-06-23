#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 1
Author: Hank Preston <hapresto@cisco.com>

example2.py
Illustrate the following concepts:
- Reading from and writing to files
- The "with" statement
- Writing to command line
- Requesting interactive user input
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from datetime import datetime

log_file = "example2.log"


def read_log(log):
    """
    Open the logfile and print contents to the terminal
    """
    with open(log, "r") as f:
        print(f.read())


def write_log(log, name):
    """
    Add new logfile entry with datestamp
    """
    # Get current date and time
    log_time = str(datetime.now())
    with open(log, "a") as f:
        f.writelines("Entry logged at: {} by {}\n".format(log_time, name))


# Entry point for program
if __name__ == '__main__':
    # Get users name
    name = input("What is your name? ")

    # Add entry to log file
    print("Adding new log entry")
    write_log(log_file, name)
    print("")

    # Access Starting Log File
    print("Log File Contents")
    print("-----------------")
    read_log(log_file)
