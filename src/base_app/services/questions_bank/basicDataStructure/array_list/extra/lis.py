# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:51:36 2018

@author: Atul Anand
"""


def lis():
    list1=[5,-2,5,-22,3,4,2,1,-11,2,3,-111]
    maxTillNow=0
    tempMax=0
    for i in range(len(list1)):
        tempMax += list1[i]
        
        if tempMax > maxTillNow:
            maxTillNow = tempMax
        if tempMax <0:
            tempMax =0

    print("maxTillNow",maxTillNow)            

lis()        

def lcs(str1="atulanand",str2="atanand"):
    pass


def coinChange(coins,val):
    
    for i in range(val):
        for coin in coins:
            