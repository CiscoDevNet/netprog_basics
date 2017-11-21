#!/usr/bin/env python

'''
This script stops, and then starts all the nodes in the 
sandbox using the VIRL APIs.  
'''

from time import sleep
from virlutils import *
from builtins import input
import sys

if __name__ == "__main__": 
    
    # Get simulation list
    nx_os_simulation = get_simulations()
    nx_os_simulation_name = list(nx_os_simulation.keys())[0]
    
    print("VIRL Simulation Name: {}\n".format(nx_os_simulation_name))
    
    # Get Simulation Node List and determine which to restart
    print("Which node would you like to restart?")    
    nodes = get_nodes(nx_os_simulation_name)
    node_key = []
    for i, node in enumerate(nodes.keys()):
        node_key.append(node)
        print("  {} - {}: Status {}".format(i, node, nodes[node]["state"]))
    print("  a - Restart All Nodes ")
    print("Enter 0 - {} to choose a node, or a for all".format(len(node_key)-1))
    # Ask user which to start
    choice = input()
    
    # Validate Users Choice.  
    try: 
        if int(choice) not in range(0, len(node_key)-1): 
            print("Invalid Choice")
            print("  Enter 0 - {} to choose a node, or a for all").format(len(node_key)-1)
            sys.exit(1)
        else: 
            choice = int(choice)
            # A single node was picked, update working nodes dictionary 
            nodes = {node_key[choice]: nodes[node_key[choice]]}
    except ValueError: 
        # A non-Integer was entered, verify it was the letter "a".  
        if str.lower(choice) != "a": 
            print("Invalid Choice")
            print("  Enter 0 - {} to choose a node, or a for all").format(len(node_key)-1)
            sys.exit(1)
    
        
    # Stop Nodes
    print("Stopping Nodes")
    action = stop_nodes(nx_os_simulation_name, nodes)
    print(action["stopped"])
    print("")
    
    # Wait for nodes to be fully stopped (state = ABSENT)
    while not test_node_state(nx_os_simulation_name, "ABSENT", test_nodes=nodes):
        print("Nodes not stopped yet")
        sleep(10)
    
    # Start Nodes
    print("Starting Nodes")
    action = start_nodes(nx_os_simulation_name, nodes)
    print(action["started"])
    print("")
    
    # Wait for nodes to be fully started (state = ACTIVE)
    while not test_node_state(nx_os_simulation_name, "ACTIVE", test_nodes=nodes):
        print("Nodes not started yet")
        sleep(10)
    
    # Done
    print("Nodes have been restarted, however it can take up to 15 minutes for all switches to fully boot and be ready.")
    print("You can monitor the startup activity at: ")    
    for node in nodes.keys():
        console = get_node_console(nx_os_simulation_name, node)
        try: 
            print("    Console to {} -> `telnet {} {}`".format(node, console["host"], console["console_port"]))
        except TypeError: 
            pass
    