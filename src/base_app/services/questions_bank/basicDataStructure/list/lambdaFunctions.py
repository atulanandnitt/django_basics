# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:18:27 2018

@author: atanand
"""

#lambda funtions

squareA_num = lambda x:x**2
print(squareA_num(4))
list1=[2,3,4,5,6,7,8,9]
squareList = list(filter(lambda x: (x**2 ),list1))
print("squareList : ",squareList)

list1=[2,3,4,5,6,7,8,9]
evenList = list(filter(lambda x: (x%2 ==0 ),list1))
oddList = list(filter(lambda x: (x%2 !=0 ),list1)) #oddList = [filter(lambda x: (x%2 !=0 ),list1)]
print(evenList)
print(oddList)


list2=[1,2,3,4]
from functools import reduce
print(reduce ( ( lambda x,y:x*y ),list2 ))
print(reduce ( ( lambda x,y:y*y ),list2 ))


print(list1+list2)

print(zip(list1,list2))