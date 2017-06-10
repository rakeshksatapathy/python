#!/usr/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positive_sum,negative_sum,zero_sum=0,0,0
for i in xrange(n) : 
    positive_sum+=1 if arr[i] > 0 else 0
    negative_sum+=1 if arr[i] < 0 else 0
    zero_sum+=1 if arr[i] == 0 else 0
positive_fraction=float(positive_sum)/n
negative_fraction=float(negative_sum)/n
zero_fraction=float(zero_sum)/n

print "%.6f" % (positive_fraction)
print "%.6f" % (negative_fraction)
print "%.6f" % (zero_fraction)

