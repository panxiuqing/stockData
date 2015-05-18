#!/usr/bin/python

__author__ = 'pxqing'

import time, random
import urllib2 as u

for H, E in [(6, 'ss'), (0, 'sz'), (3, 'sz')]:
    for i in range(0, 3000):
        time.sleep(random.random()*2)
	C = "%d%05d" % (H, i)
	print "getting", C
        try:
	    f = u.urlopen('http://table.finance.yahoo.com/table.csv?s=' + C + '.' + E, timeout=5)
	    print "writing", C
            with open('./Data/%s/%s.csv' % (E, C), 'w') as tb:
                tb.write(f.read())
        except Exception, e:
            print "get", C, e
