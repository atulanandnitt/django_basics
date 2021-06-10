# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:39:44 2018

@author: Atul Anand
"""

# Sample bash code
t = int(input())

for _ in range(t):
    str1 = input()
    dict1 = {key : str1.count(key) for key in set(str1)}
    for key1,val1 in dict1.items():
        if val1 ==2:
            print("Yes")
            break
    else:
        print("NO")