# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:52:50 2018

@author: atanand
"""

def quick_sort(arr):
    quick_sort_helper(arr,0,len(arr)-1)
    
def quick_sort_helper(arr,first,last):
    if first < last:
        splitpoint = partition(arr,first,last)
        
        quick_sort_helper(arr,first,splitpoint-1)
        quick_sort_helper(arr,splitpoint+1,last)
        
def partition(arr,first,last):
    pivotvalue=arr[first]

    leftmark=first+1
    rightmark=last        
    
    done=False
    
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1
        
        while arr[rightmark] >= pivotvalue and rightmark >=leftmark:
            rightmark -=1
        
        if rightmark < leftmark:
            done =True
              
        else:
            temp=arr[leftmark]
            arr[leftmark]=arr[rightmark]
            arr[rightmark]=temp
    
    temp=arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
    
    return rightmark


alist = [54,26,93,17,77,31,44,55,20,5,4,3,6,21,81,2,1,0]
#alist = [54,26,93,17]
quick_sort(alist)
print(alist)