import subprocess

def print_banner():
    """
    Print the colorful banner for the IP CHANGER script.
    """
    banner = """
   

    '####:'########::::::'######::'##::::'##::::'###::::'##::: ##::'######:::'########:'########::
    . ##:: ##.... ##::::'##... ##: ##:::: ##:::'## ##::: ###:: ##:'##... ##:: ##.....:: ##.... ##:
    : ##:: ##:::: ##:::: ##:::..:: ##:::: ##::'##:. ##:: ####: ##: ##:::..::: ##::::::: ##:::: ##:
    : ##:: ########::::: ##::::::: #########:'##:::. ##: ## ## ##: ##::'####: ######::: ########::
    : ##:: ##.....:::::: ##::::::: ##.... ##: #########: ##. ####: ##::: ##:: ##...:::: ##.. ##:::
    : ##:: ##::::::::::: ##::: ##: ##:::: ##: ##.... ##: ##:. ###: ##::: ##:: ##::::::: ##::. ##::
    '####: ##:::::::::::. ######:: ##:::: ##: ##:::: ##: ##::. ##:. ######::: ########: ##:::. ##:
    ....::..:::::::::::::......:::..:::::..::..:::::..::..::::..:::......::::........::..:::::..::


    =========================================
    |         Welcome to IP CHANGER         |
    |    Change the IP Address of Your NIC  |
    |			-by anonymous23	    |
    =========================================
    """
    print(banner)

def get_network_interfaces():
    """
    Get a list of network interfaces available on the system.

    :return: List of network interfaces.
    """
    try:
        result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        
        interfaces = []
        for line in lines:
            if 'mtu' in line:
                interface = line.split()[1].strip(':')
                interfaces.append(interface)
        
        return interfaces
    
    except subprocess.CalledProcessError as e:
        print(f"Failed to retrieve network interfaces: {e}")
        return []

def bring_interface_down(interface):
    """
    Bring the network interface down.

    :param interface: The network interface to bring down (e.g., 'eth0').
    """
    try:
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'], check=True)
        print(f"Interface {interface} is down.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to bring interface {interface} down: {e}")

def remove_existing_ip(interface):
    """
    Remove existing IP addresses from the network interface.

    :param interface: The network interface to configure (e.g., 'eth0').
    """
    try:
        # Get existing IP addresses
        result = subprocess.run(['ip', '-o', 'addr', 'show', interface], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')

        for line in lines:
            if 'inet' in line:
                # Extract the IP address
                ip_address = line.split()[3]
                # Remove the IP address
                subprocess.run(['sudo', 'ip', 'addr', 'del', ip_address, 'dev', interface], check=True)
                print(f"Removed IP address {ip_address} from {interface}")

    except subprocess.CalledProcessError as e:
        print(f"Failed to remove existing IP addresses: {e}")

def change_ip(interface, new_ip, netmask='255.255.255.0'):
    """
    Change the IP address of a network interface.

    :param interface: The network interface to configure (e.g., 'eth0').
    :param new_ip: The new IP address to assign.
    :param netmask: The netmask to assign (default is '255.255.255.0').
    """
    try:
        # Change the IP address
        subprocess.run(['sudo', 'ip', 'addr', 'add', f'{new_ip}/{netmask}', 'dev', interface], check=True)
        print(f"IP address of {interface} changed to {new_ip} with netmask {netmask}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change IP address: {e}")

def bring_interface_up(interface):
    """
    Bring the network interface up.

    :param interface: The network interface to bring up (e.g., 'eth0').
    """
    try:
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], check=True)
        print(f"Interface {interface} is up.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to bring interface {interface} up: {e}")

if __name__ == "__main__":
    print_banner()
    
    # Display available network interfaces
    interfaces = get_network_interfaces()
    if interfaces:
        print("\033[1;36mAvailable network interfaces:\033[0m")
        for iface in interfaces:
            print(f"\033[1;32m- {iface}\033[0m")
    else:
        print("\033[1;31mNo network interfaces found.\033[0m")
        exit(1)

    interface = input("\n\033[1;33mEnter the network interface to configure (e.g., eth0):\033[0m ")
    new_ip = input("\033[1;33mEnter the new IP address (e.g., 192.168.1.10):\033[0m ")
    netmask = input("\033[1;33mEnter the netmask (default is 255.255.255.0):\033[0m ")

    if not netmask:
        netmask = '255.255.255.0'

    bring_interface_down(interface)
    remove_existing_ip(interface)
    change_ip(interface, new_ip, netmask)
    bring_interface_up(interface)

