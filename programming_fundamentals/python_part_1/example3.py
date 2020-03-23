#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 1
Author: Hank Preston <hapresto@cisco.com>

example3.py
Illustrate the following concepts:
- Creating and using dictionaries
- Creating and using lists
- Working with for loops
- Conditional statements
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

# Example Dictionary
author = {"name": "Hank", "color": "green", "shape": "circle"}

# A list of colors
colors = ["blue", "green", "red"]

# A list of dictionaries
favorite_colors = [
                      {
                          "student": "Mary",
                          "color": "red"
                      },
                      {
                          "student": "John",
                          "color": "blue"
                      }
                  ]

# Entry point for program
if __name__ == '__main__':
    print("The author's name is {}.".format(author["name"]))
    print("His favorite color is {}.".format(author["color"]))
    print("")

    print("The current colors are:")
    for color in colors:
        print(color)
    print("")

    # Ask user for favorite color and compare to author's color
    new_color = input("What is your favorite color? ")
    if new_color == author["color"]:
        print("You have the same favorite as {}.".format(author["name"]))
        print("")

    # See if this is a new color for the list
    elif new_color not in colors:
        print("That's a new color, adding it to the list!")
        colors.append(new_color)
        # Print update message about the new colors list
        message = ("There are now {} colors in the list. ".format(len(colors)))
        message += "The color you added was {}.".format(colors[3])
        print(message)
    else: 
        pass
