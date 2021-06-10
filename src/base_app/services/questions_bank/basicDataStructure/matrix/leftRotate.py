def leftRotate(a,i,n,k):
    print("val : ",a,i,n,k)
    for _ in range(k):
        p=int(i)
        t=a[p]
        for _ in range(n-1):
            a[p]=a[p+1]
            p+=1
        a[p]=t
    
    
t=1#int(input())
for _ in range(t):
    temp=[2,2,1]#input().split()
    m=int(temp[0])
    n=int(temp[1])
    k=int(temp[2])
    a=[1,2,3,4]#input().split()
    for i in range(0,len(a),n):
        leftRotate(a,i,n,k)
    for i in a:
        print(i,end=" ")
    print("")