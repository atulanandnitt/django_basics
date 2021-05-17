# -*- coding: utf-8 -*-
"""
Created on Wed May  2 12:32:07 2018

@author: atanand
"""

import itertools

def out(n, arr, x):
	if(n<4):
		return 0
	for tup in itertools.combinations(arr, 4):
		if(sum(tup)==x):
			return 1
	return 0

t = int(input())
for m in range(t):
    n = int(input()) #no use of n in python
    arr = [int(x) for x in input().split()]
    x = int(input())
    print(out(n, arr, x))