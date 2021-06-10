# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:08:08 2018
    
    for t1 in zip(mat):
        if t1[0] > x:
            
    
@author: Atul Anand
"""

def search(mat,x):
    i =0
    n=len(mat)
    j = n-1
    
    while i<n and j >= 0:
        if mat[i][j] == x:
            return 1
        
        if mat[i][j] > x:
            j -= 1 
        else:
            i += 1
            
    return 0


mat=[[10,20,30,40],
     [15,25,35,45],
     [27,29,37,48],
     [32,33,39,50]]

x=320
print(search(mat,x)            )