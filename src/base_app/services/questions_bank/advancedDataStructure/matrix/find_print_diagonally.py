#https://practice.geeksforgeeks.org/problems/print-diagonally/0/?ref=self


t = 1#int(input())
for _ in range(t):
    n = 3#int(input())
    list1 = [1,2,3,4,5,6,7,8,9]#list(map(int, input().strip().split()))
    print(find_print_diagonally(list1,n))
    
"""
1,2,3
4,5,6
7,8,9
"""    
t = 1#int(input())
for i in range(t):
    n = 3#int(input())
    i=0
    c = 1
    arr = [1,2,3,4,5,6,7,8,9]#[int(i) for i in input().split()]
    arr.insert(0,0)
    print(arr)
    for j in range(1,2*n):
        if i <n:
            x=i
            i+=1
        else:
            x = i+n
            i+=n
            
        for x2 in range(c):
            print(arr[i+(n-1)*x2],end=' ')
        #print('yeah',c,'re',end=' ')
        if i<n:
            c+=1
        elif i>=n:
            c-=1
    print()
            
    
    
    
def find_print_diagonally(list1,n):
    m=n
    mat = [[list1[(i*n)+j]for j in range(n)] for i in range(m)]
    count =0
    solList=list()
    #count = (n-1) + (m-1) +1
    
    for i in range(m):
        for j in range(n):
            if i+j == count:
                solList[count].append(mat[i][j])
            count += 1
    return solList

t = 1#int(input())
for _ in range(t):
    n = 3#int(input())
    list1 = [1,2,3,4,5,6,7,8,9]#list(map(int, input().strip().split()))
    print(find_print_diagonally(list1,n))