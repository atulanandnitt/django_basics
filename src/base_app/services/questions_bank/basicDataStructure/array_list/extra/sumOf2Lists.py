# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 08:15:12 2018

@author: atanand
"""

items1=[1,2,3,4,5,6,7,8,9,10]
items2=[1,2,3,4,5,6,7,8,9,10]
evenList=[]
oddList=[]
solSum=[]

for item in items1:
    if item %2 ==0:
        evenList.append(item)
    else:
        continue

for item in items2:
    if item %2 !=0:
        oddList.append(item)
    else:
        continue
    
print(evenList)
print(oddList)    

i=0
for item in range(len(evenList)):
    a=evenList[i]
    b=oddList[i]
    i+=1
    solSum.append(a + b)
    
print(solSum)    


l=len(evenList)
i=0
for item in range(len(evenList)):
    a=evenList[i]
    b=oddList[l-1-i]
    i+=1
    solSum.append(a + b)
    
print(solSum) 