#code
    
"""    


def find(arr):
    m=len(arr)
    n=len(arr[0])
    for i in range(m-2,-1,-1):
        for j in range(n):
            if 0<j<n-1:
                arr[i][j]+=max(arr[i+1][j],arr[i+1][j-1],arr[i+1][j+1])
            elif j==0:
                arr[i][j]+=max(arr[i+1][j],arr[i+1][j+1])
            elif j==n-1:
                arr[i][j]+=max(arr[i+1][j],arr[i+1][j-1])
    return max(arr[0])
        
    
for i in range(int(input())):
    n=int(input())
    arr=[]
    l=list(map(int,input().split()))
    s=0
    for j in range(n):
        k=0
        arr.append([])
        while(k != n):
            arr[j].append(l.pop(0))
            k+=1
    print(find(arr))




"""
def find_path_in_matrix(arr):
    m=len(arr)
    n=len(arr[0])
    for i in range(m-1):
        for j in range(n):
            if 0<j<n-1:
                arr[i][j]+=max(arr[i+1][j],arr[i+1][j-1],arr[i+1][j+1])
            elif j==0:
                arr[i][j]+=max(arr[i+1][j],arr[i+1][j+1])
            elif j==n-1:
                arr[i][j]+=max(arr[i+1][j],arr[i+1][j-1])
    return (arr[0])
        

    
    
t = 1#int(input())
for _ in range(t):
    n = 2#int(input())
    list1= [86,177,115,193]
    mat=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = list1[(n*i)+j]
    print(mat)
    mat2=[[list1[(n*i)+j] for j in range(n)] for i in range(n)]
    print(mat2)
    print(find_path_in_matrix(mat2))