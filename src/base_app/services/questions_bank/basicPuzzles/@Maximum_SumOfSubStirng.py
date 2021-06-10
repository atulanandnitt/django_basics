# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:19:12 2018

@author: atul
"""

#largest continuous subArray
#kadane_Algo

def max(a,b):
    if a>b:
        return a
    else:
        return b

def findMaxSum(arr):
    maxSum=0
    maxTillNow=0
    for item in arr:
        maxSum +=item
        
        if maxSum < 0:
            maxTillNow=maxSum - item
            maxSum=0
    maxTillNow=max(maxTillNow,maxSum)
    print(maxTillNow)

array =[4,-3,-2,2,3,1,33,-2,-3,4,2,-6,-3,-1,3,15,2]
    
findMaxSum(array)
