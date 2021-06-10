# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:18:35 2018

@author: Atul Anand
"""

def lineNo(list1):
    print(list1)
    list2=[]

    list2= sorted(list1)
    print(list2)
    list1.sort()
    print(list1)
    
    
list1=[[20,50],
       [4,7],
       [1,8],
       [8,11],
       [15,17]]    

lineNo(list1)