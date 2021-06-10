#https://practice.geeksforgeeks.org/problems/nth-item-through-sum/0
#not able to submit

def findNthVal(list1,list2,n):
    list3=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            
            list3.append((list1[i] + list2[j] ) )
    list3.sort()
    print(list3)
    return list3[n]

t =1# int(input())

for _ in range(t):
    p,q=3,5# map(int,input())
    list1=[1,3,4,8,10]#list(map(int,input().strip().split()))
    list2=[20,22,30,40]#list(map(int,input().strip().split()))
    n=4#int(input())
    print(findNthVal(list1,list2,n))
    
    
    
"""
Example:
Input:
2
2 2
1 2
3 4
3
5 4
1 3 4 8 10
20 22 30 40
4

Output:
6
25

"""