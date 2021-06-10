# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 13:29:38 2018

@author: atul
"""

#anagram check

def isAnagram(input_str1,input_str2):
    
    input_list1=[]
    input_list2=[]
    
    input_str1=input_str1.replace(" ","")
    input_str2=input_str2.replace(" ","")
    
    """
    for chr1 in input_str1:
        input_list1.append(chr1)

    for chr2 in input_str2:
        input_list2.append(chr2)     
    
    sortedinput_list1=sorted(input_list1)
    sortedinput_list2=sorted(input_list2)
    """    

    sortedinput_list1 =  sorted(input_str1)  
    sortedinput_list2 = sorted(input_str2)
    
    sortedstr1="".join(sortedinput_list1)
    sortedstr2="".join(sortedinput_list2)
    
    print(sortedstr1)
    print(sortedstr2)
    
    if sortedstr1 == sortedstr2:
        print("{} and {} are anagram ")
        return True
    else:
        print("{} and {} are NOT anagram")
        return False
    

input_str1="atul is a good boy atul"
input_str2="altuis a good boy"
inputList=   input_str1.split() 
print("inputList ************", type(inputList))
if isAnagram(input_str1,input_str2):
    print("{} and {} are anagram %input_Str1 %input_str2")

else:
    print("{} and {} are NOT anagram %input_Str1 %input_str2")
    
    
    
    
dict1= dict([(key,inputList.count(key)) for key in inputList ])    
print(dict1)

maxValue = [key for key,value in dict1.items() if value == max(dict1.values())]
print(maxValue)  