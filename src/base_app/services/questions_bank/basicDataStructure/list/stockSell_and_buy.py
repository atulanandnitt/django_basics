# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:08:54 2018

@author: atul


print all profitable transactions
"""

#practice
#n= int(input())

#stockPrices=list(map(int,input().split()))



#stockPrices = [3,2,4,1,2,3,4,5,6,5,9]
stockPrices = [100,180,260,310,40,535,695]
print(len(stockPrices))
index =0
count =0
for item in stockPrices:
    count +=1
print(count)


localMin=list()
localMax = list()
indexOflocalMaxValue=0
global test
def findLocalMax(index,stockPrices):
    localMaxValue =0
    print("count : ",count)
    while index < count-1:
        if stockPrices[index+1] > stockPrices[index]:
            localMaxValue= stockPrices[index+1]
            indexOflocalMaxValue = index+1
            test=indexOflocalMaxValue
            #print("indexOflocalMaxValue", indexOflocalMaxValue)
        else:
            return localMaxValue
        index +=1
    return localMaxValue


while index < count-1:
    #print(stockPrices[index])
    if stockPrices[index+1] > stockPrices[index]:
        localMin.append(stockPrices[index])
        localMax.append(findLocalMax(index,stockPrices))
        #index=indexOflocalMaxValue   #this is causing infinite loop
        #print(test)
        index +=1
    
print(localMin)
print(localMax)
#print(test)

profit=list()
i=0
for item in localMax:
    profit.append(localMax[i] - localMin[i])
    i +=1

print(profit)    

"""    
    
"""

"""
localMinMax={
        localMin:None,
        localMax:None}


for index2 in stockPrices:
    if stockPrices[]
    localMin
"""