# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:20:03 2018

@author: atul
"""

#find the missing num

def findMissingNum(arr1,arr2):
    sum1,sum2=0,0
    print(arr1,arr2)
    for item1 in arr1:
        sum1 += item1
    for item2 in arr2:
        sum2+=item2
    print(sum1,sum2)
    if sum2>sum1:
        return sum2-sum1
    else:
        return sum1-sum2

arr1=[1,2,3,4,5,6,7,8,9]
arr2=[1,3,4,5,6,7,8,9]

print(findMissingNum(arr1,arr2))



print("solution through XOR")

def findMissingNum(arr1,arr2):
    result =0
    
    for num in arr1+arr2:
        result^=num
        print (result)
        
    return result

arr1=[1,2,3,4,5,6,7,8,9]
arr2=[1,3,4,5,6,7,8,9]

print(findMissingNum(arr1,arr2))


print("sol through sorting")

def finder(arr1,arr2):
    
    arr1.sort()
    arr2.sort()
    
    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
        
    return arr1[-1]

arr1=[1,2,3,4,5,6,7,8,9]
arr2=[1,2,3,4,5,7,8,9]

print(finder(arr1,arr2))

