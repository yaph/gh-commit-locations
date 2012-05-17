# -*- coding: utf-8 -*-
import re, operator
locations = {}
for line in open('unresovled_locations.txt','r'):
    loc = line.strip().lower().capitalize()
    if '' == loc: continue
    if loc not in locations:
        locations[loc] = 0
    locations[loc] += 1

locsorted = sorted(locations.iteritems(), key=operator.itemgetter(1), reverse=True)
for loc, cnt in locsorted:
    print '%s\t%d' % (loc, cnt)
