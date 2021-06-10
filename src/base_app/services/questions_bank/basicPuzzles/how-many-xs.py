# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:14:17 2018

@author: atanand
"""

#code

t= 1#int(input())

for i in range(t):
    x=3#int(input())
    n1,n2=100,250#map(int,input().strip().split())
    counter =0
    for j in range(n1+1,n2):
        str1=str(j)
        for ch in str1:
            if ch == '3':
                print(str1)
                counter +=1
                #break
    print(counter)

def occurences(i, d):
    if not d in str(i):
        return 0
    count = 0
    for c in str(i):
        if c == d:
            print("c :",c,"i ",i)
            count += 1
    return count
    
#code
for _ in range(int(input())):
    d = str(input())
    l, u = (int(i) for i in input().split())
    
    # result
    n = 0
    for i in range(l+1,u):
        n += occurences(i,d)
        
    print(n)        
        
"""        

t= 1#int(input())

for i in range(t):
    x=3#int(input())
    n1,n2=100,250#map(int,input().strip().split())
    counter =0
    for j in range(n1+1,n2):
        while j / 10 > 0:
            lastDigit=j%10
            if lastDigit == x:
                print("j: ",j,"lastDigit :",lastDigit)
                counter +=1
            j = int(j/10)
    print(counter)
    
"""    