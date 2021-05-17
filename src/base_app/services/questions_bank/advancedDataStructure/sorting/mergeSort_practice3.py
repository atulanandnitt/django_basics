# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:30:50 2018

@author: atanand
"""

def mergeSort(list1):
    
    if len(list1)>0:
        start=0
        end = len(list1)
        mid = (end - start ) //2
        
        left = mergeSort(list1[1:mid])
        right = mergeSort(list1[mid+1:])
        
        
        while left and right:
            solList.append(left)