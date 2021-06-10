#maxSubSquareMat

def maxSubSquareMat(mat):
    m=len(mat)
    n=len(mat[0])
    print(m,n)
    solMat=[]#[0 for i in range(m) for j in range(n) ]
    maxVal=0
    for i in range(m+1):
        col=[]
        for j in range(n+1):
            col.append(0)
        solMat.append(col)
    print(solMat)
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] ==0:
                solMat[i][j] = 0
            else:
                solMat[i][j] = 1 + min(solMat[i-1][j], solMat[i-1][j-1] , solMat[i][j-1])
                maxVal=max(maxVal,solMat[i][j])
    print(solMat)
    return maxVal



mat=[ [1,1,1,1,1],
     [1,1,1,0,1],
     [0,1,1,1,1],
     [1,1,1,1,0]]    

print(maxSubSquareMat(mat))    