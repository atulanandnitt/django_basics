# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 07:40:45 2018

@author: Atul Anand

https://www.youtube.com/watch?v=xtfj4-r_Ahs&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p

"""

def solution():
        
    list1=  [0,1,0,1,1,1,1]
    list2 = [1,1,1,1,1,0,1]
    
    n= len(list1)
    sum1,sum2=0,0
    maxLen =0
    
    solList =[-1 for _ in range((2*n) +1)]
    
    for i in range(len(list1)):
        sum1 += list1[i]
        sum2 += list2[i]
        currentDiff = sum1 - sum2
        diffIndex = n + currentDiff
        
        if currentDiff == 0: maxLen = i +1
        elif solList[diffIndex] == -1: solList[diffIndex] =i
        else:
            length = i - solList[diffIndex]
            if length > maxLen:
                maxLen = length
    print(maxLen)
    return maxLen
                

print(solution()            )