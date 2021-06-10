
def dp_unique_paths3(i,j,m,n):
    
    solList=[[0 for j in range(n)] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            if j ==0 or i ==0:
                solList[i][j] =1
                continue
            solList[i][j] = solList[i][j-1] + solList[i-1][j]
    
    return solList[m-1][n-1]
    
    
def uniquePath2(i,j,m,n):
    if i==m or j ==n:
        return 1
    else:
        return uniquePath2(i+1,j,m,n) + uniquePath2(i,j+1,m,n)



    
#code

def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return int(n*fact(n-1))
        
def findNoOfUniquePath1(m,n):
    return int(fact(m+n-2) /(fact(m-1)*fact(n-1)))


    
   
    
t = 1#int(input())
for _ in range(t):
    m,n = 3,4#map(int, input().strip().split())
    print(findNoOfUniquePath1(m,n))
    print(uniquePath2(1,1,m,n))
    print(dp_unique_paths3(0,0,m,n))