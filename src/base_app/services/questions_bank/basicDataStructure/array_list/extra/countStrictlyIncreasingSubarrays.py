# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:54:00 2018

@author: Atul Anand

https://www.youtube.com/watch?v=eMuC2LCoMvU&index=11&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p
"""



def countStrictlyIncreasingSubarrays(list1):
    
    count =0
    n= len(list1)
    for i in range(n):
        
        for j in range(i+1,n):
            
            if list1[j] > list1[j-1]:
                count += 1
            
        else: break
    
    return count


list1=[7,4,-3,-6,5,-99,33,22,11]

print(countStrictlyIncreasingSubarrays(list1))


"""
def countStrictlyIncreasingSubarrays(list1):
    noOfSubArrays=0
    countInASubArray =0
    start=0
    end=0
    for i in range(len(list1)-1):
        if list1[i] < list1[i+1]:
            start += 1
            end = i +1
            
        elif (list1[end] > list1[start]) :
            print("start :", start , list1[start])
            print("end :", end, list1[end])
            noOfSubArrays += 1
        
        else:
            
            start = i
            end = start
    
    return noOfSubArrays

list1=[7,4,-3,-6,5,-99,33,22,11]

print(countStrictlyIncreasingSubarrays(list1))
"""
    

def lis(list1):#sum
    sumTillNow= list1[0]
    maxSumTillNow = 0
    for i in range(len(list1)):
        if sumTillNow + list1[i]  < 0:
            sumTillNow =0
        else:
            sumTillNow += list1[i]
            
        maxSumTillNow = max(sumTillNow,maxSumTillNow)
    return maxSumTillNow

list1=[7,4,-3,-6,5,-99,33,22,11]

print(lis(list1))