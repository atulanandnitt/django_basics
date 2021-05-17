# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:06:55 2018

@author: Atul Anand
"""
def noOfWayToReturnTheChange(coins,n):
    
    solList=[0 for i in range(n+1)]
    solList[0] =1
    print(solList)
    for coin in coins:
        for j in range(coin,n+1):
            solList[j] += solList[j- coin]
    print("solList :", solList)
    
    
coins=[1,2,5,10]
n=12
print(noOfWayToReturnTheChange(coins,n))            
            




def minNoOfcoinsToReturnVal(coins,n):
    solList=[9999 for i in range(n+1)]
    solList[0] =1
    for coin in coins:
        solList[coin] =1
        for j in range(n+1):
            solList[j] = min(solList[j- coin] +1 , solList[j])
    
    for i in range(len(solList)):
        print(i , end ="")
            
    return solList



coins=[1,2,5,10]
n=12
print(minNoOfcoinsToReturnVal(coins,n))            
            