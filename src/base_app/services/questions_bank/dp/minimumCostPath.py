def findMinCostPath(mat):
    print(mat)
    m=len(mat)
    n=len(mat[0])
    print(m,n)

    for i in range(m):
        for j in range(n):
            if i==0 and j>0:
                sol[i][j] = sol[i][j-1] + mat[i][j]
            elif j ==0 :#and i >=1:
                sol[i][j] = sol[i-1][j] + mat[i][j]
    
    print(mat)
    
    
mat=[[1,3,5,8],
     [4,2,1,7],
     [4,3,2,3]
    ]    

findMinCostPath(mat)