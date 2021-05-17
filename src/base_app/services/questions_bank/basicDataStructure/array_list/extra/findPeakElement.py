# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:13:58 2018

@author: Atul Anand
"""



def findPeakElementBest(list1,low,high):#NOT WORKING
    mid =  (low + high ) //2 #low + ( (high - low) //2)
    n = len(list1)
    if ( (( mid ==0) or (list1[mid-1] <= list1[mid] )  )  and (( mid == n-1) or (list1[mid+1] <= list1[mid] ))):
        return mid
    
    elif ( mid > 0 and ( list1[mid-1]  > list1[mid]) ):
        return findPeakElementBest(list1,low,mid-1)
    
    else:
        return findPeakElementBest(list1,mid+1,high)
    
    
        
    


list1=[10,20,15,2,23,90,67]

print(findPeakElementBest(list1,0,len(list1)))




def findPeakElement(list1):
    left=list1[0]
    right= list1[2]
    peakElemList =[]
    for i in range(1,len(list1)):
        if left < list1[i]  and list1[i] >right:
            peakElemList.append(list1[i])
            left = list1[i]
            try:
                right = list1[i+2]
            except:
                continue
    return max(peakElemList)


list1=[10,20,15,2,23,90,67]

print(findPeakElement(list1))
            