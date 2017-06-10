#!/usr/bin/python

import sys
def StairCase(n):
    for i in xrange(0,n+1) :
        for j in xrange(0,n-i) :
            sys.stdout.write(' ')
        for k in xrange(0,i) :
            sys.stdout.write('#')
        sys.stdout.write('\n')
_n = int(input());
StairCase(_n)

