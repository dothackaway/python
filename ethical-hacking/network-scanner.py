#!/usr/bin/env python3

#
# Tool for discovering clients on the same network
# 1. Create arp request packet directed to broadcast MAC asking for IP
# 2. Send packet and receive response
# 3. Parse the response
# 4. Print result
#

import scapy.all as scapy, argparse, re


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range. Example: 192.168.1.1 or 192.168.1.1/24")
    options = parser.parse_args()
    regex = re.compile(r"(\w{1,3}\.){3}\w{1,3}")
    # error conditions
    if not options.target:
        # Missing required interface
        parser.error("[-] Please specify a target IP or IP range, use --help for more info.")
    elif not regex.search(options.target):
        # Target entered not accepted
        parser.error("[-] Target entered " + options.target + " not accepted.  Use --help for more info.")
    return options
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
    # Create list of clients and dictionary of client elements
    clients_list = []
    for element in ans_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list

def print_results(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Run
options = get_arguments()
scan_result = scan(options.target)
print_results(scan_result)
