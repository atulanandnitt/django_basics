# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:38:01 2018

@author: atanand
"""

def mergeSort(list1):
    
    start=0
    end=len(list1)
    mid = (start+ end ) //2
    
    if len(list1) >1:
        left = mergeSort(list1[:mid])
        right = mergeSort(list1[mid:])
    

        mergeSort(left)
        mergeSort(right)
    
    
    
list1=[4,3,5,2,6,1,8]
print(mergeSort(list1))    
    