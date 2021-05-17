# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:47:01 2018

@author: Atul Anand

https://www.youtube.com/watch?v=hoceGcqQczM&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p&index=4

"""

def minDis(list1,x,y):
    i=0
    prev=0
    min_dist = 99999#inf
    n = len(list1)
    
    for i in range(n):
        if list1[i] == x or list1[i] ==y:
            prev =i
            break
    
    for i in range(n):
        if list1[i] ==x or list1[i] ==y:
            
            if list1[prev] != list1[i] and (i - prev) < min_dist:
                
                min_dist = i- prev
                prev =i
            else:
                prev =i
    
    return min_dist


                
list1= [3,5,4,1,6,0,0,5,4,8,3]
x,y=3,6

print(minDis(list1,x,y))

                