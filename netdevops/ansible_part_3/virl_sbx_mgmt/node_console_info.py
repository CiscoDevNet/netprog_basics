#!/usr/bin/env python

'''
This script returns the telnet console info for all nodes.  
'''

from time import sleep
from virlutils import *


if __name__ == "__main__": 
    
    # Get simulation list
    nx_os_simulation = get_simulations()
    nx_os_simulation_name = nx_os_simulation.keys()[0]
    
    print("VIRL Simulation Name: {}\n".format(nx_os_simulation_name))
    
    # Get Simulation Node List     
    print("Retrieving Console Connection Details: ")
    nodes = get_nodes(nx_os_simulation_name)
    for node in nodes.keys():
        console = get_node_console(nx_os_simulation_name, node)
        try: 
            print("    Console to {} -> `telnet {} {}`".format(node, console["host"], console["console_port"]))
        except TypeError: 
            pass
        
