def lis_sum(list1):
    lis =[]#list1#[1 for item in range(len(list1))]
    solList=[]
    actualSeq=[1 for item in range(len(list1))]
    for item in list1:
        lis.append(item)
    for i in range(len(list1)):
        for j in range(i):
            if list1[j] < list1[i]:
                if lis[i] > lis[j]+list1[i]:
                    continue
                    #actualSeq[i]=i
                    #lis[i] =lis[i]
                else:
                    lis[i] = lis[j]+list1[i]
                    actualSeq[i]=j
                    solList.append(list1[i])
                    
    print(lis)
    print("actualSeq is wrong",actualSeq)
    print("solList :",solList)
    return max(lis)

    
list1=[4,6,1,3,8,4,6]    
print(lis_sum(list1))    
#actual sequence= [0,0,2,2,1,5,6]



def lis(list1):
    lis =[1 for item in range(len(list1))]
    
    for i in range(len(list1)):
        for j in range(i):
            if list1[j] < list1[i]:
                
                lis[i] = max(lis[i] , lis[j]+1)
    print(lis)
    return max(lis)

    
list1=[4,6,1,3,8,4,6]    
print(lis(list1))    
