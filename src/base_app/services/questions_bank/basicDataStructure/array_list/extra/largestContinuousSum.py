# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:35:57 2018

@author: atul
"""

#larget continuous SUM


def largestContSum(inputList):
    print(inputList)
    sumTillNow=0
    maxSumTillNow=0
    for item in inputList:
        print ("sumTillNow :   ",sumTillNow)
        print ("maxSumTillNow :   ",sumTillNow)
        if sumTillNow >=0:
            sumTillNow += item
        elif maxSumTillNow <= sumTillNow:
            maxSumTillNow = sumTillNow
        else:
            sumTillNow =item
    return maxSumTillNow


inputList=[1,2,-1,3,4,10,10,-10,-1]

print ("Whats the issue ?????:::  ",largestContSum(inputList))    



def largestContSum(inputList):
    print(inputList)
    sumTillNow=0
    maxSumTillNow=0
    for item in inputList:
        print ("sumTillNow :   ",sumTillNow)
        print ("maxSumTillNow :   ",maxSumTillNow)
        #sumBeforeNow = sumTillNow
        if sumTillNow >=0:
            sumTillNow += item
        else:
            sumTillNow =item
            
        if maxSumTillNow <= sumTillNow:
            maxSumTillNow = sumTillNow

    return maxSumTillNow


inputList=[1,2,-1,3,4,10,10,-10,-1]

print ("correct solution",largestContSum(inputList))    


# solution from 

def large_count_sum(arr):
    
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum =arr[0]
    
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        
        max_sum = max(current_sum,max_sum)
        
    return max_sum
    
inputList=[1,2,-1,3,4,10,10,-10,-1]

print (large_count_sum(inputList))    