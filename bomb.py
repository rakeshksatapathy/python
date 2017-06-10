#!/usr/bin/python

import sys
import os

def  contains_bomb(arr):
    arr2=sorted(set([x for x in arr if arr.count(x) > 1]))
    count=0
    value=0
    for i in range(len(arr2)) :        
        if i>0 and int(arr2[i]) == int(arr2[i-1])+1 and value==int(arr2[i-1]): 
            count+=1
            value=int(arr2[i])
        elif i>0 and int(arr2[i]) == int(arr2[i-1])+1 and value+1==arr2[i]: 
            count+=1
            value=int(arr2[i])
        else :
            count=0
            value=int(arr2[i])
        if count==2 :           
            print "YES"
            break
    if count < 2 :
        print "NO"

a=raw_input().strip().split()
contains_bomb(a)

