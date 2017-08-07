#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 1
Author: Hank Preston <hapresto@cisco.com>

example1.py
Illustrate the following concepts:
- Script Structure and Format
- Importing and using packages
- Variable declaration and usage
- Function creations and usage 
- Basic Error Handling
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

import sys


def doubler(number):
    """
    Given a number, double it and return the value
    """
    result = number * 2
    return result


# Entry point for program
if __name__ == '__main__':
    # Retrieve command line input
    try:
        input = float(sys.argv[1])
    except (IndexError, ValueError) as e:
        # Indicates no command line parameter was provided
        print("You must provide a number as a parameter to this script")
        print("Example: ")
        print("  python example1.py 12")
        sys.exit(1)

    # Double the provided number and print output
    answer = doubler(input)
    print(answer)
