def minNoOfCoins(coins,val):
    solList=[99999 for i in range(val+1)]
    solList[0]=0
    for i in range(len(coins)):
        for j in range(val+1):
            solList[j] = min(solList[j] , solList[j - coins[i]] +1)
    print("solList",solList)
    return solList[val]
    
def noOfWaysOfCoinChange(coins,val):
    solList=[0 for i in range(val+1)]
    solList[0]=1
    for i in range(len(coins)):
        for j in range(coins[i],val+1):
            
            solList[j] += solList[j - coins[i]]
    print(solList)    
    
coins=[1,2,3]
val=5
print(minNoOfCoins(coins,val))  
print(noOfWaysOfCoinChange(coins,12))  
  