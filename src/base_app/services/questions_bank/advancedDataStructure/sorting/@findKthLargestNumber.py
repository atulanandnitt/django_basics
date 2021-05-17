# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:44:50 2018

@author: Atul Anand
"""
def findindexOfMin(list2):
    miniInList2=min(list2)
    for i in range(len(list2)):
        if list2[i] == miniInList2:
            return i
    
def findindexOfMin_2(list2):
    return (list2.index(min(list2)))

def findKthLargestNo(list1,k):
    print(list1)
    list2=[]#size k
    list2=list1[0:k]
    indexOfMin=findindexOfMin(list2)
    print(list2)
    for i in range(k,len(list1)):
        if list1[i] > list2[indexOfMin]:
            print("updated list2 : ",list2,"   ",list2[indexOfMin])
            list2[indexOfMin]=list1[i]
            #list2.pop(indexOfMin)
            #list2.insert(list1[i],indexOfMin)
            indexOfMin=findindexOfMin(list2)
    list2.sort()            
    print(list2)
    return list2[0]
   
list1=[5,3,1,2,4]
k=4
print(findKthLargestNo(list1,k)    )