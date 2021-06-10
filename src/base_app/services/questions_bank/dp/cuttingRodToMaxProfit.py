#cuttingRodToMaxProfit


def cuttingRodToMaxProfit(lenPriceList,l):
    profitList = [0 for i in range((l) +1)]
    profitList[0] =0
    
    for item in lenPriceList:
        for j in range(1,l+1):
            #print(item , )
            profitList[j] = max( profitList[j] , item[1] + ( profitList[j - item[0] ] ) )
    
        print(profitList)
            
        
    
    return max(profitList)
    


lenPriceList=[[1,2],
              [2,5],
              [3,7],
              [4,8]] # what if dict ??

#lenPriceList=[[1,2]]
l=5# sol is 12

print(cuttingRodToMaxProfit(lenPriceList,l))