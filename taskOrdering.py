#!/usr/bin/python

import sys
import os

def  taskOrdering(arr):
    final_list=[]
    for i1 in xrange(len(arr)):
        arr2=arr[i1]
        position1 = final_list.index(arr2[0]) if arr2[0] in final_list else None
        position2 = final_list.index(arr2[1]) if arr2[1] in final_list else None
        if position2 == None and position1 == None: 
            final_list.insert(0,arr2[1])
            final_list.insert(0,arr2[0])
        elif position2 != None and position1== None:
            final_list.insert(int(position2),arr2[0])
        elif position2 == None and position1!= None:
            final_list.insert(int(position1)+1,arr2[1])
        elif position2<position1:
            final_list[position2],final_list[position1]=final_list[position1],final_list[position2]
    print final_list
    
#a=[[4,1], [3,1], [5,2], [5,1], [5,4], [3,2], [4,2], [4,3], [5,3]]
a=[[5,1],[5,2],[4,3],[4,2],[3,1],[2,1],[3,2]]
taskOrdering(a)

