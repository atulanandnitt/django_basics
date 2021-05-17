# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:59:00 2018

@author: atanand
"""

def average_of_a_stream_of_numbers(avgTillNow,nTillNow,x):
    newAvg =  (( avgTillNow * nTillNow )  + x )/ nTillNow +1
    return newAvg


n= int(input())
entered=0
while entered < n:
    enteredVal = int(input())
    entered += 1
    avg= average_of_a_stream_of_numbers(avg,entered,enteredVal)
    

import math    
def isPrime(n):
    if n >0:
        for i in range( 2,int(math.sqrt(int(n)))):
            if n % i == 0:
                return False
        else: return True

print(isPrime(11))        


list1=[1,2,3,4,5,6,7,8,9,10]
k=15
def findPairsWhoseSum(list1,k):
    set1=set(list1)
    for item in list1:
        val = (k-item)
        if val in set1:
            print("pair which sum is k =" ,k, item , val)# ,"is found.which value is "item,"and ",val)

findPairsWhoseSum(list1,k)