#!/usr/bin/python

import os
import sys
import socket
from datetime import datetime


# usage: python portConnectScanner.py 
##### Creates a socket connection and scans the specified ports ######



def portScanner(ip_host, port_host):
    s = socket.socket()
    s.settimeout(1.0)
    banner = ''
    try:
       s.connect((ip_host, port_host))  # takes a Tuple
       s.send('Hey, give me the banner!')
       banner = s.recv(1024)
       s.close()

    except: 
       print "[-] Socket error cant connect."
     
    return banner




if __name__ == "__main__":
    hosts = ['google.com']
    ports = [22, 445, 80, 443, 3389]
    try:
        for ip_host in hosts:
            for port_host in ports:
                banner = portScanner(ip_host, port_host)
                if banner:
                    print "[+] Port "+str(port_host)+" open: "+banner
                else:
                    print "[-] No open ports found"

    except: pass
