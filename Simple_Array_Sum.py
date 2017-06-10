#!/usr/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
if len(arr) != n :
    print "Invalid no. of arguments"
    raise 
else : 
    sum=0
    for i in xrange(0,n) : 
        sum+=arr[i]
    print sum       

