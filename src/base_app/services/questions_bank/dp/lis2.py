# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:08:54 2018

@author: Atul Anand
"""

#code

def find_lis(list1):
    lis =[1 for i in range(len(list1)+1)]
    
    for i in range(len(list1)):
        for j in range(i):
            if list1[i] > list1[j]:
                lis[i] += 1
    return (lis)
    
    
    
t = 1#int(input())
for _ in range(t):
    waste = 83#int(input())
    list1= [86,177,115,193,135,186,92,49,21,162,27,90,59,163,126,140,26,172,136,11,168,167,29,182,130,62,123,67,135,129,2,22,58,69,167,193,56,11,42,29,173,21,119,184,137,198,124,115,170,13,126,91,180,156,73,62,170,196,81,105,125,84,127,136,105,46,129,113,57,124,95,182,145,14,167,34,164,43,150,87,8,76,178
]
    print(find_lis(list1))