"""
Problem Statement
=================
Find the length of the longest Bitonic Sequence in a given sequence of numbers. A Bitonic sequence is a sequence of
numbers which are increasing and then decreasing.

Analysis
--------
* Runtime O(n)
Reference
---------
* http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/
"""

def bitonicSubSequence(list1):
    lisFromLeft=[1 for item in range(len(list1))]
    lisFromRight= [1 for item in range(len(list1))]
    bitonicSeq=[]
    for i in range(len(list1),0,-1):
        for j in range(len(list1)-1,i,-1):
            if list1[i] > list1[j]:
                lisFromRight[i] = max(lisFromRight[i] , lisFromRight[j] +1)
    print("lisFromRight :",lisFromRight)
            
    
    
    
    for i in range(len(list1)):
        for j in range(i):
            if list1[i] > list1[j]:
                lisFromLeft[i] = max(lisFromLeft[j] +1 ,lisFromLeft[i])
    
       
    print("lisFromLeft : ",lisFromLeft)
        
    for item1,item2 in zip(lisFromLeft,lisFromRight):
        bitonicSeq.append((item1+item2) -1)
    print("bitonicSeq : ", bitonicSeq) 
    print(bitonicSeq)
    return max(bitonicSeq)

list1=[0,6,4,5,3,8,1,9]

print(bitonicSubSequence(list1))    

