# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:26:43 2018

@author: atanand
"""

#code

def find_median_in_a_stream(mean,i,x):
    newMean = ( (mean * i) + x) /(i+1)
    return int(newMean)
    
    
t= int(input())
mean =0
for i in range(t):
    x=int(input())
    mean=find_median_in_a_stream(mean,i,x)
    print(mean)
    