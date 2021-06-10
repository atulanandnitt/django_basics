#code

def bucketSort(list1):
    str1=""
    list1.sort()
    set1=set(list1)
    dict1={key:list1.count(key) for key in set1}
    solList=[]
    print("min(dict1.keys())",min(dict1.keys()))
    print("dict1[min(dict1.keys())]",dict1[min(dict1.keys())])
    while (min(dict1.keys())) :
        for i in range(dict1[min(dict1.keys())]):
            solList.append(min(dict1.keys() ) )
        print("solList",solList)
        print("deleting",min(dict1.keys()),dict1[min(dict1.keys())])
        del(dict1[min(dict1.keys())])
    print("solList",solList)        
    for item in list1:
        str1 += str(item) +" "
    return str1[:-1]
    
    

t=1#int(input())

for _ in range(t):
    wsate=1#int(input())
    list1=[1,2,3,1,2,3,1,2,3,1,0,1,2,1,2,0,3,2,2,1,3,2]#list(map(int,input().strip().split()))
    #list1=[1,2,3,1,2,3,1,2,3,1,1,2,1,2,3,2,2,1,3,2]#not working for this i/p
    print(bucketSort(list1))