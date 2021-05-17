def findSingle(list1):
    solList=[]
    dict1={key:list1.count(key) for key in set(list1)}
    
    for key1,val1 in dict1.items():
        if val1 % 2 ==1:
            solList.append(key1)
            
    return solList
    
    
t = 1#int(input())

for _ in range(t):
    list1=[1,1,1,3]#list(map(int,input().strip().split()))
    
    print(findSingle(list1))