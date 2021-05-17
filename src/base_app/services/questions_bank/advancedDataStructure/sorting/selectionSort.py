# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 08:04:06 2018

@author: atanand
"""

#Queue basic:

def selectionSort(arr):
    #for every slot in array
    for fillslot in range(len(arr)-1,0,-1 ):
        positionOfMax=0
        
        for location in range(1,fillslot+1):
            #set maximum location
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
            
            print("fillslot",fillslot,"location",location)
            
        temp = arr[fillslot]
        arr[fillslot]=arr[positionOfMax]
        arr[positionOfMax]=temp
        #print("positionOfMax",positionOfMax)
        


alist = [54,26,93,17,77,31,44,55,20,5,4,3,6,21,81,2,1,0]
#alist = [54,26,93,17]
selectionSort(alist)
print(alist)        


