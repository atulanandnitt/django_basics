#code
def solList(l):
    n=len(l)
    k=min(l)
    for i in range(0,n):
        if(l[i]-k>0):
            print(n-i,end=" ")
            k=l[i]
    print()
        
t=1#int(input())


for _ in range(t):
    n=3#int(input())
    list1=[5,1,1,2,3,5]#list(map(int,input().strip().split()))
    solList(list1)



"""

def solList(list1):

    lenList=[]
    while max(list1) >1:
        mini=min(list1)
    
        
        for i in range(len(list1)):
            list1[i] -= mini
            
        tempLength=0    
        for i in range(len(list1)):
            if list1[i] != 0:
                tempLength +=1
        
        lenList.append(tempLength)
        
        print(lenList)
        solStr=""
        for item in lenList:
            solStr += str(item)

    return solStr

t=1#int(input())

for _ in range(t):
    n=3#int(input())
    list1=[5,1,1,2,3,5]#list(map(int,input().strip().split()))
    
    print(solList(list1))
"""