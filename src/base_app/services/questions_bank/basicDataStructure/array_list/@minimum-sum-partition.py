# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:32:08 2018

@author: Atul Anand
"""
def solve2(list1):
    size = sum(list1)
    solList = (size+1)*[0]
    solList =[0 for i in range(len(list1)+1)]
    solList[0] = 1
    for x in list1:
        for y in range(size,-1,-1):
            if solList[y] == 1:
                solList[y+x] = 1
    mini = 1000000
    for x in range(size+1):
        if solList[x] == 1:
            if abs(size-2*x)  < mini:
                mini = abs(size-2*x)
    return mini
    
t = 1#int(input())    
for z in range(t):
    n = 4#int(input())
    arr = [36,7,46,40]#list(map(int,input().strip().split()))
    print(solve2(arr))
    
    
def solve1(arr):
    size = sum(arr)
    barr = (size+1)*[0]
    #solList =[0 for i in range(len(list1)+1)]
    barr[0] = 1
    for x in arr:
        for y in range(size,-1,-1):
            if barr[y] == 1:
                barr[y+x] = 1
    mini = 1000000
    for x in range(size+1):
        if barr[x] == 1:
            if abs(size-2*x)  < mini:
                mini = abs(size-2*x)
    return mini

t = 1#int(input())    
for z in range(t):
    n = 4#int(input())
    arr = [36,7,46,40]#list(map(int,input().strip().split()))
    print(solve1(arr))
    

