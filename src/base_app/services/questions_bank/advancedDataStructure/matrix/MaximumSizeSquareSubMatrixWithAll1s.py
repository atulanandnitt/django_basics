# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:29:19 2018

@author: Atul Anand
"""

def MaximumSizeSquareSubMatrixWithAll1s(mat):
    print(mat)
    
    solMat=[[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    print(len(mat), len(mat[0]))
    
    print(len(solMat), len(solMat[0]))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(solMat, i, j)
            if i ==0 or j ==0 or mat[i][j] ==0 :
                solMat[i][j] = mat[i][j]
                continue
                
            elif mat[i][j] != 0:
                solMat[i][j] = max(mat[i-1][j-1], mat[i-1][j], mat[i][j-1]) + 1
                    

    print(solMat)
    

mat=[ [0 ,1, 1,0,1],
     [1,1,0,1,0],
     [0,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,0,1],
     [0,0,0,0,0]]
    
solMat=[[0 for j in range(len(mat))] for i in range(len(mat[0]))]
    
print(solMat)  
 

MaximumSizeSquareSubMatrixWithAll1s(mat)    