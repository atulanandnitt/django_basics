# -*- coding: utf-8 -*-
"""
Created on Wed May 23 23:25:36 2018

@author: atanand
"""

#code

def findMaxSum(list1):
  m=0
  c=0
  s=0
  for i in range(len(list1)):
    print(m,c,s)
    s=max(m,c)
    m=c+list1[i]
    c=s
  return (max(c,m)) 
  
t = 1#int(input())

for _ in range(t):
    waste=4#int(input())
    list1=[5,5,10,100,10,5]#list(map(int,input().strip().split()))
    print(findMaxSum(list1))