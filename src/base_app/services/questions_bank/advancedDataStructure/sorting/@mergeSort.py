# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 19:23:34 2018

@author: atul

Merge Sort can be used to sort an unsorted list or to merge two sorted lists.


"""
def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = int(len(alist)/2)  #mid = len(alist)//2

       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       print(type(mid),"@@@@@@@@@@@@@",mid)
       print("lefthalf is ",lefthalf)
       print("righthalf is ",righthalf)
       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           #print("inside 1st while)
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging **********",alist)

alist = [54,26,93,17,77,31,44,55,20,5,4,3,6,21,81,2,1,0]
#alist = [54,26,93,17]
mergeSort(alist)
print(alist)

"""
Merge Sort works both with a large and small number of elements making it more efficient than Bubble, 
Insertion and Selection Sort. This comes at a price since Merge Sort uses additional space to produce
 a sorted list. The worst case runtime complexity of Merge Sort is o(nlog(n)) and 
 the space complexity is n. Try to merge two sorted lists
"""