# -*- coding: utf-8 -*-
#practice CoinchangeDP

def coinChange(coins,n,q):
    solList=[0 for i in range(q+1)]
    solList[0]=1
    for i in range(n):
        for j in range(coins[i],q+1):
            solList[j] += solList[j - coins[i]]
    
    return solList[q]

coins=[2,5,7]
print(coinChange(coins,3,60))    

coins=[1,2,3]
val=5
print(minNoOfCoins(coins,val))  
print(noOfWaysOfCoinChange(coins,12))  