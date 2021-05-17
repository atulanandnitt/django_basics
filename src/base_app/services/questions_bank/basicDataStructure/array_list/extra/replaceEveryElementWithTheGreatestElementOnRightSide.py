# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:42:57 2018

@author: Atul Anand
"""

def replaceEveryElementWithTheGreatestElementOnRightSide(list1):
    solList=[list1[-1]]
    maxTillNow = list1[-1]
    for i in range(len(list1)-1,-1,-1):
        if maxTillNow < list1[i]:
            maxTillNow = list1[i]
        solList.insert(0,maxTillNow)
    return solList

list1=[16,17,4,3,5,2]            
print(replaceEveryElementWithTheGreatestElementOnRightSide(list1))            