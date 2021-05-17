# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:04:04 2018

@author: Atul Anand
"""
import itertools
n =10
list1= [i for i in range(11)]
i=0
for t1 in itertools.combinations(list1,2):
    if t1[0] + t1[1] ==n:
        print(t1)
    print(i)
    i += 1
        
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] + list1[j] == n:
            print(list1[i], list1[j])
        if list1[i] + list1[j] > n:
            print("saved")
            break
       