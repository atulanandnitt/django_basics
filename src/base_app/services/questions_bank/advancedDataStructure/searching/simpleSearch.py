# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:45:57 2018

@author: atanand
"""

# sequentioal searching

def seq_search_Unordered(list1,toSearch):
    for item in list1:
        if item == toSearch:
            return True
    return False


list1=[3,4,5,6,7,8,2,5,2,9,12,43]
a=3
b=53
print(seq_search_Unordered(list1,a))
print(seq_search_Unordered(list1,b))



def seq_search_Ordered(list1,toSearch):
    for item in list1:
        if item == toSearch:
            return True
        elif item > toSearch:
            return False
    return False

list1=[3,4,5,6,7,8,2,5,2,9,12,43]
list1.sort()
a=3
b=53
print(seq_search_Unordered(list1,a))
print(seq_search_Unordered(list1,b))