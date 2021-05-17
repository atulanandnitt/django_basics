# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:50:10 2018

@author: atanand
"""

#practice merge sort

def mergeSort(arr):
    if len(arr)>1:
        midpoint=len(arr)//2
        lefthalf=arr[:midpoint]
        righthalf=arr[midpoint:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i,j,k=0,0,0
        
        print("lefthalf : ",lefthalf,"righthalf : ",righthalf,"arr : ",arr)
        
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]>righthalf[j]:
                arr[k]=righthalf[j]
                j +=1
            else:
                arr[k]=lefthalf[i]
                i+=1
            k+=1
        
        while i<len(lefthalf):
            arr[k]=lefthalf[i]
            i +=1
            k +=1
        
        while j <len(righthalf):
            arr[k]=righthalf[j]
            j +=1
            k +=1
    print ("arr  : ",arr)
    return arr

arr=[4,5,3,6,2,7,1,8,9]
mergeSort(arr)            