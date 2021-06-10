# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:52:05 2018

@author: atul
"""

def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
for i in range(11):
    print(fact(i))