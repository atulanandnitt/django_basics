# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 05:55:28 2018

@author: atul
"""

#unique characters

def unique_char(s):
    return len(set(s))==len(s)

s="abcdef"
if unique_char(s):
    print("string ",s,"consists of unique charecters")
else:
    print("string ",s,"DOES NOT consists of unique charecters")    
    
 
def unique_char2(s):
    setA=set()
    
    for item in s:
       if item in setA:
           return False
       else:
           setA.add(item)
    
    
    return len(set(s))==len(s)

    
s=input()
if unique_char2(s):
    print("string ",s,"consists of unique charecters")
else:
    print("string ",s,"DOES NOT consists of unique charecters")       