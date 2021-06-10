# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 07:11:03 2018

@author: Atul Anand
"""

def matrixRotation(mat):
    

    print(*mat)   
    print(mat)       
    for t1 in (zip(*mat)):
        for i in range(len(t1)):
            print(t1[len(t1)-i-1] , end=" ")
        print()
            
mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]            
matrixRotation(mat)
            