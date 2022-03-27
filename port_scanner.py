# Use: scan other machine(s) and tell wether is has open port(s)


import socket
from IPy import IP


def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        # time to connect to different ports differs
        sock.connect((ip_address, port))
        print(f'Port {port} is open')
    except:
        print(f'Port {port} is closed')


def convert_ip(ip_addr):
    try:
        return IP(ip_addr)
    except ValueError:
        return socket.gethostbyname(ip_addr)


if __name__ == '__main__':
    ip_address = convert_ip(input('Enter target to scan: '))
    for port in range(80, 90):
        scan_port(ip_address, port)
