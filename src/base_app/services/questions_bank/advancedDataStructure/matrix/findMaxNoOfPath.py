# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:35:40 2018

@author: Atul Anand
"""




n,m=4,4
board=[[((n*i)+j)for j in range(m) ] for i in range(n)]
print(board)

#code

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
    
def number_of_unique_paths(m,n):
    return int((fact(m+n-2)/(fact(m-1) * fact(n-1) ) ))


#dp without recursion
def dp_unique_paths(i,j,m,n):
    
    solList=[[0 for j in range(n)] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            if j ==0 or i ==0:
                solList[i][j] =1
                continue
            solList[i][j] = solList[i][j-1] + solList[i-1][j]
    
    return solList[m-1][n-1]
    



def uniquePath(i,j,m,n):
    if i==m or j ==n:
        return 1
    else:
        return uniquePath(i+1,j,m,n) + uniquePath(i,j+1,m,n)

    
    
t = int(input())
for _ in range(t):
    m,n = map(int, input().strip().split())
    print(uniquePath(0,0,m,n))
    #print(number_of_unique_paths(m,n))
    #print(dp_unique_paths(0,0,m,n))