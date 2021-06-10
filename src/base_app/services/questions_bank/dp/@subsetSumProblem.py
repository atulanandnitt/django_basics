# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:20:25 2018

@author: atanand
"""



def noOfWaysOfSubSet(coins,val):
    solList= [0 for j in range(val+1)]
    solList[0] =1
    
    for coin in coins:
        for j in range(coin,val+1):
            solList[j] += solList[j-coin]
    
    print("solList :",solList)
    return solList[-1]
    
coins=[6,8]
coins=[2,3,8]
val=11
print(noOfWaysOfSubSet(coins,val))    
    

def subsetSumProblemWithHelpOf_noOfWaysOfSubSet(list1,k):
    if noOfWaysOfSubSet(list1,k) > 0:
        return 1
    else:
        return 0
    
list1=[2,3,4,5,6,1,8]
val=11

print(subsetSumProblemWithHelpOf_noOfWaysOfSubSet(list1,val))  

    
