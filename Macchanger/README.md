# MAC Changer

A simple Python script to change the MAC address of a network interface on a Linux system. This can be useful for privacy, testing, or bypassing certain network restrictions.

## Warning

Changing your MAC address can disrupt your network connection and may be against network policies. Always ensure you have permission to change your MAC address on the network you're using.

## Prerequisites

- Python 3
- `ifconfig` command (available through the `net-tools` package)

## Installation

1. **Clone the repository** (or download the script directly):

    ```bash
    git clone https://github.com/mr-anonymous-hash/cli-tools.git
    cd macchanger
    ```

2. **Install `net-tools`** if it is not already installed:

    ```bash
    sudo apt-get install net-tools
    ```

3. **Make the script executable** (optional but recommended):

    ```bash
    chmod +x macchanger.py
    ```

## Usage

Run the script with the network interface and new MAC address as arguments:

```bash
sudo ./macchanger.py <interface> <new_mac>

