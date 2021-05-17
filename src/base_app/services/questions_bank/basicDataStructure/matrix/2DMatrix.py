# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:29:57 2018

@author: atanand
"""

#code


#leftRotation
def solFun(m,n,mat,k):
    matrix=[]
    l=0
    for i in range(M):
        col=[]
        for j in range(N):
            col.append(mat[l])
            l+=1
        matrix.append(col)
    print(matrix)
    solMat=[]
    for i in range(N):
        col=[]
        for j in range(M):
            col.append(0)
        solMat.append(col)
        
    for i in range(m):
        for j in range(n):
            solMat[j][i] =matrix[i][j]
    return solMat

            
    
    
t=1# int(input())

for _ in range(t):
    M,N,K =2,2,1# map(int,input().strip().split())
    mat=[1,2,3,4]#list(map(int,input().strip().split()))
    
    #matrix[M][N]=[None for i in range(M*N) for j in range(N)]

    #print(item)
    sol=solFun(M,N,mat,K)
    print(sol)