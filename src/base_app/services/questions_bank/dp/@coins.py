# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:24:17 2018

@author: Atul Anand
"""

def miniNoOfCoinsNeeded(coins,val):
    
    solList=[9999 for _ in range(val+1)]
    
    for coin in coins:
        solList[coin] =1
        for j in range(coin,val+1):
            solList[j] = min(solList[j] , solList[j-coin]+1)
    
    print(solList)
    
coins=[1,2,5]
val=5

print(miniNoOfCoinsNeeded(coins,val))    
coins=[7,2,3,6]
val=13
print(miniNoOfCoinsNeeded(coins,val))    



def noOfWaysOrReturn(coins,val):
    
    solList=[0 for _ in range(val+1)]
    solList[0] =1
    for coin in coins:
        #solList[coin] +=1
        
        for j in range(coin,val+1):
            solList[j] += solList[j-coin]
    return solList
            
coins=[2,5]
val=13
coins = [3,5,7]
val=10
print(noOfWaysOrReturn(coins,val))    


