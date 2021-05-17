#https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0/?ref=self

#code



#code
for i in range(1):
    n=6#int(input())
    a=list1=[16,17,4,3,5,2]#list(map(int,input().split()))
    l=[]
    l.append(a[n-1])
    print("l  is",l)
    m=a[n-1]
    for j in range(n-2,-1,-1):
        if(a[j]>m):
            l.insert(0,a[j])
            m=a[j]
    print(*l)    
    
    
    
    
    
    
def leaders(list1):
    leadersList=[]
    prev=0
    nextItem=0
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            print(list1[i], list1[j])
            if list1[i] < list1[j]:
                #j=len(list1)
                #continue
                break
            nextItem=list1[i]
        if prev != nextItem:
            leadersList.append(nextItem)
            prev=nextItem
            
    print("leadersList : ",leadersList)            
    return leadersList

t=1#int(input())

for _ in range(t):
    waste=1#int(input())
    list1=[16,17,4,3,5,2]#list(map(int,input().strip().split()))
    
    print(leaders(list1))
    
    
str1="My NAme is Atul"
print(str1.lower())    
ch=""
for j in range(5):
    for i in range(len(str1)):
        if str1[i] == "M":
            break
        print("will never be printed")