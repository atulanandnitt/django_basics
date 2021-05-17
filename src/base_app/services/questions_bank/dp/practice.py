# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:13:10 2018

@author: Atul Anand
"""

def trapWater(list1):
    left=[0 for i in range(len(list1))]
    right=[0 for i in range(len(list1))]
    left[0]=list1[0]
    right[-1] = list1[-1]
    
    for i in range(len(list1)):
        left[i]= max(left[i-1],list1[i])
    
    for i in range(len(list1)-2,-1,-1):
        right[i] = max(right[i+1],list1[i])
    water=0
    for i in range(len(list1)):
        water += min(left[i],right[i]) - list1[i]
        
    return water

list1=[5,2,0,5]
print(trapWater(list1))