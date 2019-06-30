#!/usr/bin/python


import os
import sys

# usage: python pythonscript.py ip port protocol
# lookup for domain name 

class Domain:
    def __init__(self, domain, port, protocol):
   	# stores the variabled passed inside two variables
        self.domain = domain
        self.port = port
	self.protocol = protocol
	
    # defines a method to build a url
    def URL(self):
	if self.protocol == 'https':
            URL = 'https://'+self.domain+':'+self.port+'/'
        if self.protocol == 'http':
	    URL = 'http://'+self.domain+':'+self.port+'/'
	    return URL

	# sets up a method to lookup resolve domain to IP using host comamndvia os.system
    def lookup(self):
        os.system("host "+self.domain)
        return domain.lookup()





if __name__=="__main__":
    script = sys.argv[0]
    ip = sys.argv[1]
    port = sys.argv[2]
    protocol = sys.argv[3]

    print "[+] Script name is: "+script
    print "[+] IP is: "+ip+" and port is: "+port
       
    domain = Domain(ip, port, protocol)
    domain.lookup()
   


