#!/usr/bin/python

import os, sys, socket   
import httplib, urllib    # if for web service

# usage: python pseudocodeFuzz.py <RHOST> <RPORT>
# or use ./pseudocodeFuzz.py <RHOST> <RPORT>


######## basic starter python script for fuzzer ##########

def pseudoFuzzer(RHOST, RPORT):
    # buffer string implemented until potential crash
    buffer = 'x41'*50

    # create connection to send buffer
    while True:
        try:
        # send buffer then increment by 50
            buffer = buffer + 'x41'*50
        except:
            print "Buffer length: "+len(buffer)
            print "Cannot connect to service... Crashed??"



######### main ###########
if __name__ == "__main__":
    RHOST = sys.argv[1]
    RPORT = sys.argv[2]
    pseudoFuzzer(RHOST, RPORT)
