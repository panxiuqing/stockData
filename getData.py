__author__ = 'pxqing'

import urllib2 as u
for H, E in [(6, 'ss'), (0, 'sz'), (3, 'sz')]:
    for i in range(0, 3000):
        C = "%d%05d" % (H, i)
        try:
            f = u.urlopen('http://table.finance.yahoo.com/table.csv?s=' + C + '.' + E)
            with open('./Data/%s/%s.csv' % (E, C), 'w') as tb:
                tb.write(f.read())
        except u.HTTPError:
            print "Not find %s" %C
