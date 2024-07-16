#!/usr/bin/python3

import subprocess
import re
import argparse

def get_current_mac(interface):
    result = subprocess.run(['ifconfig', interface], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        return None

    mac_address = re.search(r'(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})', result.stdout)
    if mac_address:
        return mac_address.group(0)
    else:
        print(f"Could not find MAC address for interface {interface}")
        return None

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(['sudo', 'ifconfig', interface, 'down'])
    subprocess.run(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['sudo', 'ifconfig', interface, 'up'])

def main():
    parser = argparse.ArgumentParser(description="MAC Address Changer")
    parser.add_argument("interface", help="Network interface to change MAC address for")
    parser.add_argument("new_mac", help="New MAC address")

    args = parser.parse_args()

    current_mac = get_current_mac(args.interface)
    if current_mac:
        print(f"Current MAC address for {args.interface} is {current_mac}")

        change_mac(args.interface, args.new_mac)

        updated_mac = get_current_mac(args.interface)
        if updated_mac == args.new_mac:
            print(f"[+] MAC address was successfully changed to {updated_mac}")
        else:
            print(f"[-] MAC address did not change. Current MAC address is {updated_mac}")

if __name__ == "__main__":
    main()

