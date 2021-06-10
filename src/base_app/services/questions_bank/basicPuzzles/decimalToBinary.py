# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:14:37 2018

@author: atanand
"""

#convert base10 to base2,base8 and base16


def lineNo(list1):
    print(list1)
    list1.sort()
    prev=[]
    for item in list1:
        if prev == []:
            prev= item
            continue
        
        
        if item[0] < prev[1]:
            prev[1]
    
    
list1=[[20,50],
       [4,7],
       [1,8],
       [8,11],
       [15,17]]    

lineNo(list1)