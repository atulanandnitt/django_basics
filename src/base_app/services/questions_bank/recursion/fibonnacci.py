# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:53:53 2018

@author: atul
"""

#fibonacci

def fib_recursion(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)
    

for i in range(11): #111
    print(i,"  " ,fib_recursion(i))    
    

def fib_iter_atul(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    i=2
    a=[0,1,1]
    while i <n:
        sol=a[i-1] + a[i-2]
        a.append(sol)
        i +=1
    
    return a[i-1]   

print("fib_iter_atul :  " ,fib_iter_atul(5))      
for i in range(11): #111
    print(i,"  " ,fib_iter_atul(i))    
    
def fib_iter(n):
    a,b = 0,1

    for i in range(n):
        a,b = b,a+b
    return a

for i in range(11): #111
    print(i,"  " ,fib_iter(i))



#cache
n=111
cache=[None]*(n+1)     #cache=[]....whats the issue ????
def fib_dyn(n):
    
    #base Case
    if n==0 or n==1:
        return 1
    
    
    #Check cache
    if cache[n] !=None:
        return cache[n]
    
    
    #Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

print("fib_dyn")
for i in range(111): #less than n
    print(i,"  " ,fib_dyn(i))


n=111
cache=[]#[None]*(n+1)     #cache=[]....whats the issue ????
#cache= [1,12,3,1,3]
