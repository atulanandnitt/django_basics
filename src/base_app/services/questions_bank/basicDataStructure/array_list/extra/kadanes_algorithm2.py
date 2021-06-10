# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 21:56:49 2018

@author: Atul Anand
"""

def kadane(list1):
    maximum = curMax = list1[0]
    for i in range(1, len(list1)):
        curMax = max(list1[i], curMax+list1[i])
        maximum = max(curMax, maximum)
    return maximum
    
for _ in range(1):
    waste = 1#int(input())
    list1 = [1,2,-8,3,6,-9,-2,-2,5,-3]#list(map(int, input().strip().split()))
    #list1=[-1,-2,-3,-4]
    #list1 = list(map(int, input().strip().split()))
    print(kadane(list1))
    
    
str1="atulanand"
for i in range(len(str1)):
    for j in range(i+1, len(str1)):
        print(str1[i:j])
subStr1=[ [str1[i:j] for i in range(len(str1))]  for j in range(i+1,len(str1))]
print(subStr1)

subStr1=[[str1[i:j] for i in range(len(str1))] for j in range(i+1,len(str1))]    
print(subStr1)