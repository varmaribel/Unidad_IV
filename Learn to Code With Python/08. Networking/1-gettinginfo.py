"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

import socket

def get_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    print("Host name = %s" % host_name)
    print("Ip Address = %s" % ip_address)

if __name__ == '__main__':
    get_info()
