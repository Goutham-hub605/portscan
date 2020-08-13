#!/usr/bin python

import socket
from termcolor import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = input("Enter your ip to Scan: ")

def scan(port):
    if s.connect_ex((ip, port)):
        print (colored(str(port) + "/tcp\t Closed", 'red'))
    else:
        print (colored(str(port) + "/tcp\tOpened", 'green'))

try:
    for port in range(65535):
        scan(port)

except KeyboardInterrupt as kb:
    print (colored("[!]Process Stopped", 'blue'))
