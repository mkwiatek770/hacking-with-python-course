# Use: scan other machine(s) and tell wether is has open port(s)


import socket
from IPy import IP


def scan_port(ip_address, port) -> bool:
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        # time to connect to different ports differs
        sock.connect((ip_address, port))
        return True
    except:
        False

def convert_ip(ip_addr):
    try:
        return IP(ip_addr)
    except ValueError:
        return socket.gethostbyname(ip_addr)


if __name__ == '__main__':
    targets = input("[+] Enter target(s) to scan (split multiple targets with','): ")
    for ip_address in targets.split(','):
        print('Scanning: ', ip_address)
        open_ports_counter = 0
        for port in range(1, 100):
            if scan_port(convert_ip(ip_address.strip()), port):
                print(f'[+] {ip_address} Port {port} is open')
                open_ports_counter += 1
        if open_ports_counter == 0:
            print(f'[-] {ip_address} no ports from range [1-100] are open')
