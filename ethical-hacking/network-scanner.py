#!/usr/bin/env python3

#
# Tool for discovering clients on the same network
# 1. Create arp request packet directed to broadcast MAC asking for IP
# 2. Send packet and receive response
# 3. Parse the response
# 4. Print result
#

import scapy.all as scapy

#
# scan() function to create a broadcast packet
#
def scan(ip):
    # arp_request = scapy.arping(ip)

    # Create ARP packet instance using scapy
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # send request packet, srp(), function
    # srp() returns 2 lists: answered and unanswered packets
    ans_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("________________________________________________")
    print("\tIP\t\tMAC Address\n------------------------------------------------")

    for element in ans_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)



scan("192.168.43.1/24")
