#lis

#return length
def lis(list1):
    print(list1)
    lis=[1 for i in range(len(list1) +0)]

    for i in range(len(list1)+0):
        for j in range(0,i):
            if list1[i] > list1[j]  and lis[i] < 1+ lis[j]:
                lis[i] = lis[j] +1
    print(lis)
    return max(lis)

list1=[4,5,3,6,2,7,1,8,9]

print(lis(list1))
                


def lis_Sum(list1):
    print(list1)
    lis=list1#[1 for i in range(len(list1) +0)]

    for i in range(len(list1)+0):
        for j in range(0,i):
            if list1[i] > list1[j]  and lis[i] < list1[i]+ lis[j]:
                lis[i] = list1[j]+ lis[j]
    print(lis)
    return max(lis)



def findMaxSumOfIncreasingSubSeq(list3):
    lis=[]
    for item in list3:
        lis.append(item)
    #lis=list3 will bring wrong result

    print("list 1: ",list3)
    for i in range(len(list3)):
        for j in range(i):
            if list3[i] > list3[j]:# and lis[i] < lis[j] +list1[i]:
                lis[i] = max(lis[j] + list3[i] , lis[i])
                print("lis: ",lis, list3)
            #print("lis ",lis)
    maxSumOfIncreasingSubSeq =max(lis)
    print(lis)
    return maxSumOfIncreasingSubSeq    
    
list1=[4,5,3,6,2,7,1,8,9]

print(findMaxSumOfIncreasingSubSeq(list1))    





def lcs(str1,str2,m,n):
    if n==0 or m==0:
        return 0
    elif str1[m-1] == str2[n-1]:
        return 1 + lcs(str1,str2,m-1,n-1)
    else:
        return max(lcs(str1,str2,m-1,n),lcs(str1,str2,m,n-1))
    
str1="AtulAnand"
str2="Atuland"
print(lcs(str1,str2,len(str1),len(str2)))   
print(lcs("Atul Anand","Atul and",10,8))    

            
            
            
def lcs(X,Y,m,n):#str1:X str2:Y m=len(str1) n=len(str2)
    if m==0 or n==0:
        return 0
    
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X,Y,m-1,n-1)
    
    else:
        return max(lcs(X,Y,m-1,n), lcs(X,Y,m,n-1))
    
str1="AtulAnand"
str2="Atuland"
print(lcs(str1,str2,len(str1),len(str2)))              
            