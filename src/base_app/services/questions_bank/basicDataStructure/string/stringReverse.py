# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 10:28:25 2018

@author: atanand
"""

#https://practice.geeksforgeeks.org/problems/reverse-the-string/0/?ref=self
#code

def reverseStr2(str1):
    str2=""
    for char1 in str1:
        str2 = char1 + str2
    return str2

def reverseStr(str1):
    list1=[]
    for char1 in str1:
        list1.append(char1)
    #str2=""
    for i in range(len(list1)//2):
        list1[-1-i],list1[i] = list1[i],list1[-1-i]
    return "".join(list1)
    
    
t=int(input())

for _ in range(t):
    str1=input()
    print(reverseStr(str1))