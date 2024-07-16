# IP Changer

A Python script to change the IP address of a network interface on a Linux system. This script provides a colorful banner and a step-by-step process to safely change the IP address of your network interface card (NIC).

## Features

- Display available network interfaces.
- Bring network interfaces down and up.
- Remove existing IP addresses from interfaces.
- Change the IP address and netmask of a network interface.
- Colorful banner for a pleasant user experience.

## Prerequisites

- Python 3
- `ip` command (available through the `iproute2` package)

## Installation

1. **Clone the repository** (or download the script directly):

    ```bash
    git clone  https://github.com/mr-anonymous-hash/cli-tools.git
    cd ipchanger
    ```

2. **Make the script executable** (optional but recommended):

    ```bash
    chmod +x ipchanger.py
    ```

## Usage

Run the script with the following command:

```bash
sudo ./ipchanger.py
