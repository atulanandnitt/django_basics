# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:20:09 2018

@author: Atul Anand
"""



def majorityElement(list1):
    dict1 = {key:list1.count(key) for key in set(list1)}
    n= len(list1)
    for key,val in dict1.items():
        if val > n //2:
            return key
    else:
        return None
    


list1=[1,1,1,1,1,1,11,1,1,2]
print(majorityElement(list1))



list1=[1,3,2]
print(majorityElement(list1))    