# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 22:44:23 2018

@author: atul
"""


n=111
cache=[]#[None]*(n+1)     #cache=[]....whats the issue ????
#cache= [1,12,3,1,3]
def fib_dyn_atul(n):
    
    #base Case
    if n==0 or n==1:
        return 1
    
    cache= [0,1]

    try:
        return cache[n-1]
    except:
        #Keep setting cache
        sol=fib_dyn_atul(n-1) + fib_dyn_atul(n-2)
        cache.append(sol)
        return sol

print("fib_dyn_atul(3)  " ,fib_dyn_atul(1))
for i in range(111): #less than n
    print(i,"  " ,fib_dyn_atul(i))

