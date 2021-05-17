# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 01:28:30 2018

@author: Atul Anand
"""

#code

def findMajorityElement(list1):
    dict1 = {key:list1.count(key) for key in set(list1)}
    print(dict1)
    dict2 = {key:list1.count(key) for key in set(list1) if list1.count(key) > len(list1)//2}
    print(dict2)
    for key1,val1 in dict1.items():
        if val1 > len(list1) //2:
            return key1
    else:
        return -1
    
    """
    allValues = dict1.values()
    if max(allValues) > len(list1) //2:
        return 1
    else:
        return -1
    """

list1 = [3,1,3,3,2]
print(list1.index(2))
    
    
    
t = 1#int(input())
for _ in range(t):
    waste = 5#int(input())
    list1 = [3,1,3,3,2]#list(map(int, input().strip().split()))
    print(findMajorityElement(list1))