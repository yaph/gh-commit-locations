# -*- coding: utf-8 -*-
import re, operator
locations = {}
totalcnt = 0
for line in open('unresolved_locations.txt','r'):
    loc, cnt = line.rsplit(',', 1)
    cnt = int(cnt.strip())
    loc = loc.strip().lower()
    if '' == loc: continue
    if loc not in locations:
        locations[loc] = 0
    locations[loc] += cnt
    totalcnt += cnt

print totalcnt

locsorted = sorted(locations.iteritems(), key=operator.itemgetter(1), reverse=True)
for loc, cnt in locsorted:
    print '%s\t%d' % (loc, cnt)
