# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:24:07 2018

@author: Atul Anand

https://www.youtube.com/watch?v=hySR1exD5PE&index=7&list=PLqM7alHXFySEQDk2MDfbwEdjd2svVJH9p

"""

def NumberOccurringOddNumberofTimes(list1):
    dict1 = {key: list1.count(key) for key in list1}
    
    for key,val in dict1.items():
        if val %2 ==1:
            return key
    else:
        return None
    
    
list1=[1,1,1,1,1,1,1,2,2,2,2]

print(NumberOccurringOddNumberofTimes(list1))    