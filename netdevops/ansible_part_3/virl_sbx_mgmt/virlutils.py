#!/usr/bin/env python

'''
Basic wrappers for the VIRL API
'''

import requests 

simengine_host = "http://10.10.20.160:19399"
virl_user = "guest"
virl_password = "guest" 


def get_simulations(): 
    u = simengine_host + "/simengine/rest/list"
    r = requests.get(u, auth=(virl_user, virl_password))
    return r.json()["simulations"]

def get_nodes(simulation): 
    u = simengine_host + "/simengine/rest/nodes/{}".format(simulation)
    r = requests.get(u, auth=(virl_user, virl_password))
    return r.json()[simulation]

def stop_nodes(simulation, nodes): 
    u = simengine_host + "/simengine/rest/update/{}/stop?".format(simulation)
    node_list = []
    for node in nodes.keys():
        node_list.append("nodes={}".format(node))
    node_list = "&".join(node_list)
    u += node_list
    r = requests.put(u, auth=(virl_user, virl_password))
    return r.json()

def start_nodes(simulation, nodes): 
    u = simengine_host + "/simengine/rest/update/{}/start?".format(simulation)
    node_list = []
    for node in nodes.keys():
        node_list.append("nodes={}".format(node))
    node_list = "&".join(node_list)
    u += node_list
    r = requests.put(u, auth=(virl_user, virl_password))
    return r.json()

def test_node_state(simulation, target_state, test_nodes=None):
    nodes = get_nodes(simulation)
    if test_nodes == None: 
        test_nodes = nodes
    for node in test_nodes.keys(): 
        if not nodes[node]["state"] == target_state:
            return False
    return True

def get_node_console(simulation, node):
    node_key = "guest|{}|virl|{}".format(simulation, node)
    u = simengine_host + "/roster/rest"
    r = requests.get(u, auth=(virl_user, virl_password))
    roster = r.json()
    for node in roster.keys():
        if node == node_key: 
            try: 
                return {"host": roster[node]["SimulationHost"], "console_port": roster[node]["PortConsole"]}
            except KeyError: 
                pass

def kill_simulation(simulation): 
    u = simengine_host + "/simengine/rest/stop/{}".format(simulation)
    r = requests.get(u, auth=(virl_user, virl_password))
    return "{} {}".format(r.status_code, r.text)

def launch_simulation(simulation_name, simulation_data): 
    u = simengine_host + "/simengine/rest/launch?session={}".format(simulation_name)
    headers = {"Content-Type": "text/xml;charset=UTF-8"}
    r = requests.post(u, auth=(virl_user, virl_password), headers = headers, data = simulation_data)
    return "{} {}".format(r.status_code, r.text)

