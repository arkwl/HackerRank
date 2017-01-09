#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
total = -sys.maxint-1
for i in range(0, 4):
    for j in range(0, 4):
        #print (str(arr[i][j])+" "+ str(arr[i][j+1])+ " "+ str(arr[i][j+2])+" "+str(arr[i+1][j+1])+" "+str(arr[i+2][j])+" "+str(arr[i+2][j+1])+" "+str(arr[i+2][j+2])) #debug
        candidate = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        
        if candidate > total:
            total = candidate
            #print str(total)+" "+str(i)+" "+str(j)
            
print total
