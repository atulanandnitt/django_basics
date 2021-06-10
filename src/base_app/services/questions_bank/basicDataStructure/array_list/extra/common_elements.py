
def commonElement(a1, a2, n1, n2):
    i, j=0, 0
    ans=[]
    while(i<n1 and j<n2):
        if a1[i]<a2[j]:
            i+=1
        elif a1[i]>a2[j]:
            j+=1
        elif a1[i] == a2[j]:
            ans.append(a1[i])
            i+=1
            j+=1
    return ans

t=1#int(input())
while(t>0):
    n1, n2, n3=(6,5,8)#tuple(map(int, input().strip().split()))
    a1=[1,5,10,20,40,80]#list(map(int, input().strip().split()))
    a2=[6,7,20,80,100]#list(map(int, input().strip().split()))
    a3=[3,4,15,20,30,70,80,120]#list(map(int, input().strip().split()))
    ans1_2, ans1_2_3=[], []
    ans1_2=commonElement(a1, a2, n1, n2)
    print("ans1_2", ans1_2)
    ans1_2_3 = commonElement(ans1_2, a3, len(ans1_2), n3)
    for i in ans1_2_3:
        print(i, end=" ")
    if len(ans1_2_3)==0:
        print(-1, end="")
    print()
    t-=1
    
    
"""    
def common(a1, a2, n1, n2, ans1):
    i, j=0, 0
    while(i<n1 and j<n2):
        if a1[i]<a2[j]:
            i+=1
        elif a1[i]>a2[j]:
            j+=1
        else:
            ans1.append(a1[i])
            i+=1
            j+=1


t=1#int(input())
while(t>0):
    n1, n2, n3=tuple(map(int, input().strip().split()))
    a1=list(map(int, input().strip().split()))
    a2=list(map(int, input().strip().split()))
    a3=list(map(int, input().strip().split()))
    ans1, ans2=[], []
    common(a1, a2, n1, n2, ans1)
    common(ans1, a3, len(ans1), n3, ans2)
    for i in ans2:
        print(i, end=" ")
    if len(ans2)==0:
        print(-1, end="")
    print()
    t-=1
    
"""    