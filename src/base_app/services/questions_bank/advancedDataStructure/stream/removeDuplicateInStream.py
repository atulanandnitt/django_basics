# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:40:25 2018

@author: Atul Anand
"""

dict1=dict()

def removeDuplicateInStream(stream1):
    for item in stream1:
        if item in dict1.keys():
            del(dict1[item])
        else:
            dict1[item] =1
    keys1= dict1.keys()
    
    return keys1

stream1=["Ted", "John", "Mark", 'Ted', "David"]
print(removeDuplicateInStream(stream1))