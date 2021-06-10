# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:25:12 2018

@author: atul
"""


n=111
#cache= [0,1]

def fib_dyn_atul(n):
    
    #base Case
    if n==0:
        return 0
    
    if n==1:
        return 1
    cache= [0,1]
    try:
        return cache[n]
    except IndexError:
        sol=fib_dyn_atul(n-1) + fib_dyn_atul(n-2)
        cache.insert(n,sol)
        return sol

print("fib_dyn_atul")
for i in range(112): #less than n
    print(i,"  " ,fib_dyn_atul(i))
