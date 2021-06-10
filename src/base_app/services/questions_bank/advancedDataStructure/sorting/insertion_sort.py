# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:28:41 2018

@author: atanand
"""

#insertion_sort

def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        
        currentvalue =arr[i]
        position =i
        
        while position >0 and arr[position -1] > currentvalue:
            arr[position] = arr[position -1]
            
            position = position -1
            print(arr,currentvalue)
        
        arr[position] = currentvalue
    return arr



arr=[5,4,6,3,7,2,8,1,9]

print(insertion_sort(arr))