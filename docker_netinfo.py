#!/usr/bin/python

""" Getting, formatting and presenting network information from container.
    
Notice: 
- module must be ported to Python3
- Docker 1.9v+ required (http://dockr.ly/23OzX2h)
"""

import json
import subprocess
import sys

try:
    CONTAINER = sys.argv[1]
except Exception as e:
    print "\n\tSpecify the container name, please.\n\t\tEx.:  script.py my_container\n"
    sys.exit(1)

# inspecting container via Subprocess
proc = subprocess.Popen(["docker","inspect",CONTAINER], 
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.STDOUT)

out = proc.stdout.read()        # reading output
json_data = json.loads(out)[0]  # load Subprocess output as JSON, getting the first index of list [0]

net_dict = {}
for network in json_data["NetworkSettings"]["Networks"].keys():
    net_dict['mac_addr']  = json_data["NetworkSettings"]["Networks"][network]["MacAddress"]
    net_dict['ipv4_addr'] = json_data["NetworkSettings"]["Networks"][network]["IPAddress"]
    net_dict['ipv4_net']  = json_data["NetworkSettings"]["Networks"][network]["IPPrefixLen"]
    net_dict['ipv4_gtw']  = json_data["NetworkSettings"]["Networks"][network]["Gateway"]
    net_dict['ipv6_addr'] = json_data["NetworkSettings"]["Networks"][network]["GlobalIPv6Address"]
    net_dict['ipv6_net']  = json_data["NetworkSettings"]["Networks"][network]["GlobalIPv6PrefixLen"]
    net_dict['ipv6_gtw']  = json_data["NetworkSettings"]["Networks"][network]["IPv6Gateway"]
    for item in net_dict:
        if net_dict[item] == "" or net_dict[item] == 0:
            net_dict[item] = "null"
    print "\n[%s]" % network
    print "\n{}{:>13} {:>14}".format(net_dict['mac_addr'],"IP/NETWORK","GATEWAY")
    print "--------------------------------------------"
    print "IPv4 settings:{:>16}/{:<5}  {}".format(net_dict['ipv4_addr'],net_dict['ipv4_net'],net_dict['ipv4_gtw'])
    print "IPv6 settings:{:>16}/{:<5}  {}".format(net_dict['ipv6_addr'],net_dict['ipv6_net'],net_dict['ipv6_gtw'])

