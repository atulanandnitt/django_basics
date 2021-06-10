# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 14:08:44 2018

@author: atul
"""

#sentence reversal

def sentenceReversal(inputStr):
    inputList = inputStr.strip().split()
    #inputList = inputStr.split().strip() not possible as 'list' object has no attribute 'strip'
    length = len(inputList)
    print(length)
    outputList=[]
    i=0
    while i < length:
        outputList.append(inputList[length -1-i])
        i+=1
        
    print('type(inputList)',type(inputList),inputList)
    print('type(outputList)',type(outputList),outputList)
    #inputList=map(list,inputStr.split())
    #print(inputStr.split()) 

"""
    for item in inputStr.split():
        inputList.append(item)
    
    print(inputList)
    
    for item in inputStr:
        inputList.append(item)

    for item in inputList:
        print(item)
"""    
    
sentenceReversal("My name is inputStr")    


