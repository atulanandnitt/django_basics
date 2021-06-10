# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:31:21 2018

@author: atul
"""

#reverse charecters in the word
str1="My name is Atul"
i=0
solList=[]

while i<len(str1):
    solList.append(str1[len(str1)-1-i])
    i +=1

str2="".join(solList)    
print(str2)



#reverse charecters in the word: Recursion

def reverse(s):
    
    if len(s) <=1:
        return s
    
    return reverse(s[1:]) + s[0]

print(reverse("hello world"))



#reverse words in a sentence:

def reverse(str1):
    i=0
    reverseList=[]
    while i < len(str1):
        reverseList.append(str1[len(str1) -1 - i])
        i +=1
    reverseStr ="".join(reverseList)
    return (reverseStr)

str1="My name is Atul"
i=0
intersolList=[]

while i<len(str1):
    intersolList.append(str1[len(str1)-1-i])
    i +=1

for item in intersolList:
    solList.append(reverse(item))


str2="".join(intersolList)    
print(str2)
