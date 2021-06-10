# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:55:59 2018

@author: atanand
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:53:36 2018

@author: atanand
"""

#Binary Search:

def binarySearch(arr,elem):
    first=0
    last=len(arr)-1
    found =False
    
    while first <= last and not found:
        mid = (first + last) //2
        
        if arr[mid] == elem:
            found= True
        else:
            if arr[mid] > elem:
                last=mid-1
            else:
                first=mid+1
    return found

arr=[1,2,3,4,5,6,7,8,9]
elem=11

print(binarySearch(arr,elem)  )