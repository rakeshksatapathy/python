#!/usr/bin/python

from __future__ import print_function
import sys

def StairCase(n):
    for i in xrange(n+1) : 
        for j in xrange(n-i) : 
            print (' ',end='',sep='')
        for k in xrange(i) : 
            print ('#',end='',sep='')
    print ('\n',end='',sep='')
_n = int(input());
StairCase(_n)

