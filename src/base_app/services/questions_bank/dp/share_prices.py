# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:54:36 2018

@author: Atul Anand
"""

def get_max_profit(stock_prices):
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_price in stock_prices:
        
        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
        
        # Ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        print(max_profit)

    return max_profit


list1=[11-i for i in range(11)]
#list1=[11+i for i in range(11)]
#list1=[11+i for i in range(11)]
print(get_max_profit(list1))




def findMaxProfit_from_share_good(list1):
    print(list1)
    tempMin= 9999
    #maxProfitTillNow=[0]
    maxProfit=[]
    for i in range(len(list1)):
        if list1[i] < tempMin:
            tempMin = list1[i]
        print(tempMin)
        maxProfit.append(list1[i] - tempMin)
        

    print(maxProfit)
    return max(maxProfit        )


list1=[11-i for i in range(11)]
#list1=[11+i for i in range(11)]
#list1=[11+i for i in range(11)]
print(findMaxProfit_from_share_good(list1))



def findMaxProfit_from_share(list1):
    tempMin= 9999
    maxProfitTillNow=0
    maxProfit=0
    for i in range(len(list1)):
        if list1[i] < tempMin:
            tempMin = list1[i]
        
        maxProfitTillNow = list1[i] - tempMin
        
        maxProfit = max(maxProfit,maxProfitTillNow)
        print(maxProfit)
    
    return maxProfit        

list1=[11-i for i in range(11)]
print(findMaxProfit_from_share(list1))



