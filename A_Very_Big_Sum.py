#!/usr/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum=0
for i in xrange(0,n) : 
    sum+=arr[i]
print sum

