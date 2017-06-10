# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python

import sys

def Maximum_Perimeter_Triangle(n,arr) :
    combo3_list=[]
    triangle_list=[]    
    for i in xrange(n-1) : 
        if arr[i]+arr[i+1]>arr[i+2] and arr[i+1]+arr[i+2]>arr[i] and arr[i+2]+arr[i]>arr[i+1] : 
            combo3_list.append([arr[i],arr[i+1],arr[i+2]])
    for i in xrange(len(combo3_list)) : 
        triangle_list.append(sum(combo3_list[i]))
    max_value=max(triangle_list)
    for i in xrange(len(triangle_list)) :
        if triangle_list[i]=max_value : 
            index_value.append(i)
    if len(index_value)=1 : 
        print combo3_list[i]

