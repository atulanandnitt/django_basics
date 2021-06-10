# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:51:14 2018

@author: Atul Anand
"""

n=4
m=3

mat=[[(n*i)+(j+1) for j in range(n)] for i in range(m)]
print(mat)

def spiralPrint(mat):
    m=len(mat)
    n=len(mat[0])
    print(m ,n)
    sc,ec=0,n
    sr,er=0,m
    while sc<ec and sr<er:
        #go left
        for j in range(sc,ec):
            print(mat[sr][j])
        sc += 1
        
        #go down
        for i in range(sr,er):
            print(mat[i][ec])
        ec -= 1
        
        #go right
        for j in range(ec,sc):
            print(mat[sr][j])
        er -= 1
        
        #go up
        for i in range(er,sr):
            print(mat[i][sc])
        sc += 1
        
    
spiralPrint(mat)    