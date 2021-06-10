#https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle/0

def result(a,n,k):
    max_r = 0
    max_l = 0
    max_top = 0
    max_bot = 0
    curr_max = 0

    for l in range(k):
        b = [0]*n
        for r in range(l,k):
            m = 0
            max_arr = 0
            st = 0
            e = 0
            s = 0
            for i in range(n):
                b[i] += a[i][r]
                m += b[i]
                if max_arr < m:
                    max_arr = m
                    st = s
                    e = i
                if m<0:
                    m = 0
                    s = i+1
            if max_arr > curr_max:
                curr_max = max_arr
                max_top = st
                max_bot = e
                max_r = r
                max_l = l
    print (curr_max)
    
t = 1#int(input())
for _ in range(t):
    m,n =4,5# list(map(int,input().split()))
    a = [1,2,-1,-4,-20,-8,-3,4,2,1,3,8,10,1,3,-4,-1,1,7,-6]#list(map(int,input().split()))
    b = []
    for i in range(m):
        b.append(a[i*n:(i+1)*n])
        
    print(b)
    
    c=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(a[m*i + j])
        c.append(row)
    print(c)
    
    a = b
    (result(a,m,n))
