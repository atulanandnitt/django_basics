# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:45:15 2018

@author: atul
"""

#anagram by dictionary

def isAnagramDic(inputstr1,inputstr2):
    inputstr1 = inputstr1.replace(" ","").lower()
    inputstr2 = inputstr2.replace(" ","").lower()
    """
    inputList1,inputList2=[],[]
    for item in inputstr1:
        inputList1.append(item)

    for item in inputstr2:
        inputList2.append(item)
    """    
    inputList1=sorted(inputstr1)
    inputList2=sorted(inputstr2)
    
    dict1 = dict([(key,inputList1.count(key)) for key in set(inputList1)])
    dict2 = dict([(key,inputList2.count(key)) for key in set(inputList2)])
    
    print("dict1",dict1)
    print("dict2",dict2)
    if dict1 == dict2:
        print("Anagram")
    else:
        print("NOT anagram")

inputstr1="my name IS atul"
inputstr2="Atul is My NAme"


inputstr1.lower()
inputstr2.lower()

isAnagramDic(inputstr1,inputstr2)