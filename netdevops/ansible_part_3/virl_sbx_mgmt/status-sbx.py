#!/usr/bin/env python

'''
This script checks the status of all nodes
sandbox using the VIRL APIs.  
'''

from time import sleep
from virlutils import *


if __name__ == "__main__": 
    
    # Get simulation list
    nx_os_simulation = get_simulations()
    nx_os_simulation_name = list(nx_os_simulation.keys())[0]
    
    print("VIRL Simulation Name: {}\n".format(nx_os_simulation_name))
    
    # Get Simulation Node List     
    nodes = get_nodes(nx_os_simulation_name)
    for node in nodes.keys():
        print("{}: Status {}".format(node, nodes[node]["state"]))
    print(" ")
        