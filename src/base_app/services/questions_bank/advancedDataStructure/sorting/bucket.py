# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:42:00 2018

@author: atul
"""

aList=[3,4,2,1,5]

sortedList=[]

for item in aList:
    print(item)
    sortedList.insert(item-1,item)


print(sortedList)    