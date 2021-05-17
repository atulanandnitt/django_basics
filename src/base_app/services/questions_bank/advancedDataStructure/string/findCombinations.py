# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:03:17 2018

@author: Atul Anand
"""


#code

import itertools

def findCombinations(str1):
    list1=list(str1)
    solStr=""
    tempStr2=""
    for t1 in itertools.permutations(list1,len(str1)):
        tempStr=""
        for item in t1:
            tempStr += item
        
        tempStr2 = str(tempStr) +" "
        
    
        solStr = solStr + tempStr2 
    solStr=solStr.strip()
    solList= solStr.split(" ")
    solList.sort()
    return " ".join(solList)
    
t=int(input())
for _ in range(t):
    str1= input()
    print(findCombinations(str1))
    
    
    

import itertools

def findCombinations(str1):
    list1=list(str1)
    solStr=""
    tempStr2=""
    for t1 in itertools.permutations(list1,len(str1)):
        tempStr=""
        for item in t1:
            tempStr += item
        
        tempStr2 = str(tempStr) +" "
        print(str(tempStr2))
    
        solStr = solStr + tempStr2
    return solStr.strip()
    
t=1#int(input())
for _ in range(t):
    str1="ABCD"# input()
    print("sol")
    print(findCombinations(str1))
    
    
#code

import itertools

def findCombinations(str1):
    list1=list(str1)
    solStr=""
    tempStr2=""
    for t1 in itertools.combinations(list1,len(list1)):
        tempStr=""
        for item in t1:
            tempStr += item
        
        tempStr2 = str(tempStr) +" "
        #print(str(tempStr2))
    
        solStr = solStr + tempStr2
    return solStr.strip()
    
t=int(input())
for _ in range(t):
    str1= input()
    print(findCombinations(str1))    