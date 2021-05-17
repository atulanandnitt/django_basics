# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 22:34:05 2018

@author: Atul Anand
"""

#code

def subarray_with_given_sum(list1, n):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if sum(list1[i:j]) ==n:
                t1 = list()
                t1.append(i+1)
                t1.append(j)
                return t1
    return -1
    
    


t = 1#int(input())
for _ in range(t):
    waste,n=42,468#map(int, input().strip().split())
list1 = [135,101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134]#list(map(int, input().strip().split()))
print(sum(list1[38:44]))
    t1 = subarray_with_given_sum(list1, n)
    print(t1)
    #print(t1[0],t1[1])