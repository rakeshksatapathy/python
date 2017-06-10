#!/usr/bin/python

import sys

def Time_Conversion(n) : 
    hh1,mi1,ss1=n.split(':')
    hh1=int(hh1.strip())
    mi1=int(mi1.strip())
    if ss1[2:]=='PM' :
        if hh1==12 :
            hh1+=0 
        else :
            hh1+=12 
    elif ss1[2:]=='AM' :
        if hh1==12 :
            hh1=0 
    print '%02d:%02d:%s' %(hh1,mi1,ss1[:2])
time = raw_input().strip()
Time_Conversion(time)

