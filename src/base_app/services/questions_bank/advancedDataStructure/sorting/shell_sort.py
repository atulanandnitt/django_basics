# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:40:32 2018

@author: atanand
"""

#shell_sort
def shell_sort(arr):
    sublistcount= len(arr)//2
    
    while sublistcount >0:
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)
        
        print('after increments of size : ',sublistcount)
        print('the list is ',arr)
        sublistcount = sublistcount //2
    return arr
        

def gap_insertion_sort(arr,start,gap):
    for i in range(start +gap, len(arr),gap):
        currentvalue = arr[i]
        position =i
        
        while position >=gap and arr[position -gap] >currentvalue:
            arr[position] =arr[position -gap]
            position = position - gap
            
        arr[position] = currentvalue
        


arr=[5,4,6,3,7,2,8,1,9]

print(shell_sort(arr))