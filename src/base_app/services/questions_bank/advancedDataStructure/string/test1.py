# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:09:02 2018

@author: atul
"""

 #print(inputStr.split()) 
     
inputStr="My name is inputStr"

inputList=[]
for item in inputStr:
    print(item)
    #inputList.append(item)



for item in inputStr.split(" "):
    #print(item)
    inputList.append(item)

print(inputList)

"""
for item in inputList:
    print(item)
   
"""