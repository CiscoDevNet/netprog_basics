#!/usr/bin/env python

'''
'''

from time import sleep
from virlutils import *


if __name__ == "__main__":

    # Get simulation list
    nx_os_simulation = get_simulations()

    # See if a simulation is active
    if len(nx_os_simulation) > 0:
        nx_os_simulation_name = nx_os_simulation.keys()[0]

        print("Current VIRL Simulation Name: {}\n".format(nx_os_simulation_name))
        print("Killing VIRL Simulation")
        print(kill_simulation(nx_os_simulation_name))
        print("Waiting 20 seconds to clear simulation")
        sleep(20)
        print("")

    poap_virl_file = open("ansible_part_3.virl", "r")
    poap_sim_name = "ansible_part_3"

    print("Launching New Simulation")
    print(launch_simulation(poap_sim_name, poap_virl_file.read()))
    sleep(5)

    # Wait for nodes to be fully started (state = ACTIVE)
    while not test_node_state(poap_sim_name, "ACTIVE"):
        print("  Nodes not started yet")
        sleep(10)
    print("")

    # Print Console Information for Nodes
    print("Retrieving Console Connection Details: ")
    nodes = get_nodes(poap_sim_name)
    for node in nodes.keys():
        console = get_node_console(poap_sim_name, node)
        try:
            print("    Console to {} -> `telnet {} {}`".format(node, console["host"], console["console_port"]))
        except TypeError:
            pass
