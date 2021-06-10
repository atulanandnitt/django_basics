# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:33:12 2018

@author: Atul Anand
"""

def heapify(list1,n,i):#max heap
    l= 2*i +1
    r = 2*i +2
    indexOfLargest =0
    if l<n and list1[l]>list1[i]:
        indexOfLargest = l
    if r<n and list1[r] > list1[indexOfLargest]:
        indexOfLargest =r
    
    for i in range(n-1,-1,-1):
        heapify(list1,n,i)
    
    for i in range(n-1,0,-1):
        heapify(list1,i,0)
        
def heapSort(list1):
    for 


list1=[5,3,1,2,4]
heapSort(list1)        