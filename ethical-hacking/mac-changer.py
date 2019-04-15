#!/usr/bin/env python3
# subprocess module "call"
import subprocess
import optparse
import re
#
# Functions
#
def get_arguments():
    # parser as OptionParser instance
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()

    # error conditions
    if not options.interface:
        # Missing required interface
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        # Missing required new mac
        parser.error("[-] Please specify a new MAC, use --help for more info.")

    # return options object
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    # subprocess.call("ifconfig", shell=True)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"(\w\w:){5}\w\w", ifconfig_result.decode("utf-8"))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address from interface: " + interface)


# Script run

# Receive program arguments
options = get_arguments()
# Print current MAC
current_mac = get_current_mac(options.interface)
if str(current_mac) != "None":
    print("[+] Current MAC = " + str(current_mac))
else:
    exit(0)
# Change to new MAC
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not change.")
