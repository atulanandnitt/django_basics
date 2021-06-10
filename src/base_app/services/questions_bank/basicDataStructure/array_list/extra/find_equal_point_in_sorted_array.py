# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:39:05 2018

@author: Atul Anand
"""

#code

def find_equal_point_in_sorted_array(list1):
    mini = min(list1)
    maxi = max(list1)
    for i in range(len(list1)):
        if list1[i]-mini == maxi - list1[i]:
            return i
    else:
        return -1


def find_equal_point_in_sorted_array2(a):    

    index={}
    sort=[]
    for i,v in enumerate(a):
        if v not in index:
            index[v]=i
            sort.append(v)
    s=len(sort)
    print(-1 if s%2==0 else index[sort[(s//2)]])    
    
t = 1#int(input())

for _ in range(t):
    waste = 42#int(input())
    list1 = [1,3,4,5,6,12,13,17,19,22,23,25,27,28,28,35,36,37,39,43,46,48,54,59,62,63,65,68,68,70,70,72,79,82,83,92,92,93,95,96,96,100
]#list(map( int, input().strip().split()))
    print(list1[19], min(list1), max(list1))
    print(find_equal_point_in_sorted_array2(list1))