#!/usr/bin/env python3

#
# Tool for discovering clients on the same network
# 1. Create arp request packet directed to broadcast MAC asking for IP
# 2. Send packet and receive response
# 3. Parse the response
# 4. Print result
#

import scapy.all as scapy

def scan(ip):
    # Create ARP packet using scapy
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())


scan("192.168.43.230")
