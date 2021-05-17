# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:08:07 2018

@author: Atul Anand


https://www.youtube.com/watch?v=NyRZm1pzNmQ&index=5&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p
"""

def leaders_best(list1):
    leaderList=[list1[-1]]
    maxTillNow=list1[-1]
    
    for i in range(len(list1)-2,-1,-1):
        if list1[i] > maxTillNow:
            maxTillNow = list1[i]
            leaderList.insert(0,list1[i])
    return leaderList


    
list1=[16,17,4,3,5,2]
print(leaders_best(list1))            


    
def leaders(list1):
    leaderList=[list1[-1]]
    for i in range(len(list1)-2,-1,-1):
        if list1[i] > max(list1[i+1:]):
            leaderList.insert(0,list1[i])
    return leaderList
        #for j in range(i,len(list1)):

list1=[16,17,4,3,5,2]
print(leaders(list1))            



