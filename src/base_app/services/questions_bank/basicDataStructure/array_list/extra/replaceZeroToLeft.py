# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:48:43 2018

@author: Atul Anand
"""

def replaceZeroToLeft(n):
    str1=str(n)
    solStr1=""
    for i in range(len(str1)):
        if str1[i] =="0":
            solStr1 = str1[i] + solStr1
        else:
            solStr1 += str1[i]
            
    return solStr1
            
def replaceZeroToLeft2(n):
    str1=str(n)
    l = len(str1)
    for i in range(l):
        if str1[i] =="0":
            str1 = str1[i]+str1[:i]+str1[i+1:]
        
            
    return str1
                    
    
    
    
print(replaceZeroToLeft(101101)    )
print(replaceZeroToLeft2(111001)    )

