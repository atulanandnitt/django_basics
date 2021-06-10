# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:12:01 2018

@author: atul
"""

#largest subsequence:

arr=[1,-24,7,3,-7,-11,9]

def findLargestSeq(arr):
    #start=0
    tillNowSum =0
    maxSoFar =0
    end =0
    index =0
    
    for item in arr:
        
        
        if tillNowSum < 0:
            tillNowSum =0
            maxSoFar = tillNowSum
            print("maxSoFar", maxSoFar)
        
        tillNowSum += item
            #start = index+1
        index +=1
        print("tillNowSum" , tillNowSum)
    return maxSoFar


sol= findLargestSeq(arr)
print("sol is: ",sol)