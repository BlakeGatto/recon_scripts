#!/usr/bin/python

import sys
import optparse
from spider import webspider as myspider

# usage: python  webCrawler.py <>


######## Creates a crawler for spidering a web application ########


def webCrawler(URLs):
    for line in open(URLs, 'r'):
        URL = line.strip()
        links = myspider(b=URL.strip(), w=200, d=5, t=5)
        l_count = len(links[0])
        l_specs = URL+": has link count: "+str(l_count)
        print "[+] Crawler results for: "+URL
        print l_specs
        for link in links[1]:
            print link



########### main ##############
if __name__ == "__main__":

'''
# HARDCODE <file_with URLs> FIX THIS #
Optparse allows building command line switches.
Then sets usage to '-r' and stored as variable URLs.
Then opens file at command line and try to spider.
'''
    parser = optparse.OptionParser(sys.argv[0]+' '+'-r <file_with URLs>')    
    parser.add_option('r', dest='URLs', type='string', help='specify target file with URLs')
    (options, args) = parser.parse_args()
    URLs = options.URLs

    if (URLs == None):
        print parser.usage
        sys.exit(0)
    else:
        webCrawler(URLs)
        
