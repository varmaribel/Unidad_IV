"""GITI9072-e"""
"""Maribel Vargas Exiga"""
"""Daniela Alejandra Vargas Palomino"""

import socket
import sys

def get_info(host_name = 'www.tutsplus.com3'):
    if(host_name == ''):
        host_name = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(host_name)

        print("Host name = %s" % host_name)
        print("Ip Address = %s" % ip_address)
    except socket.gaierror as e1:
        print("Couldn't connect to host_name: %s -Error: %s" % (host_name, e1))
    except socket.error as e2:
        print("Connection error: %s" % e2)

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        get_info()
    else:
        get_info(sys.argv[1])
