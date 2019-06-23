from ncclient import manager
from netmiko import ConnectHandler
import xmltodict
import requests
from pprint import pprint

router = {"ip": "127.0.0.1",
          "port": "2225",
          "user": "vagrant",
          "pass": "vagrant"}

headers = {"Accept": "application/yang-data+json"}

u = 'https://{}:{}/restconf/data/ietf-interfaces:interfaces/"interface=GigabitEthernet2'
u = u.format(router["ip"], router["port"])


r = requests.get(u,
                 headers=headers,
                 auth=(router["user"], router["pass"]),
                 verify=False)
pprint(r.text)

api_data = r.json()
interface_name = api_data["ietf-interfaces:interface"]["name"]
interface_name


router = {"ip": "127.0.0.1", "port": 2223,
          "user": "vagrant", "pass": "vagrant"}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
</filter>
"""

m = manager.connect(host=router["ip"],
                    port=router["port"],
                    username=router["user"],
                    password=router["pass"],
                    hostkey_verify=False)

interface_netconf = m.get_config("running", netconf_filter)
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]["interfaces"]["interface"]

pprint(interface_python["name"]["#text"])


interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

pprint(interface_python["interfaces"]["interface"]["name"]["#text"])


router = {
    'device_type': 'cisco_ios',
    'host':   '127.0.0.1',
    'user': 'vagrant',
    'pass': 'vagrant',
    'port': 2222
}

net_connect = ConnectHandler(ip=router["host"],
                             port=router["port"],
                             username=router["user"],
                             password=router["pass"],
                             device_type=router["device_type"]
                             )

interface_cli = net_connect.send_command("show run int Gig2")

pprint(interface_cli)
