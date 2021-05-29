# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:08:49 2018

@author: atul
"""

def findSubString(input_str):
    sorted_list=sorted(input_str)#input_str.sort()
    sorted_str ="".join(sorted_list)
    print(sorted_str,type(sorted_str))
    length=len(sorted_str)
    subSting =[sorted_str[i:j+1] for i in range(length) for j in range(i,length)]
    print(subSting)
    vowel=['a','e','i','o','u']
    sol_List=[]
    for item in subSting:
        length_item = len(item)
        if item[0] in vowel and item[length_item-1] not in vowel :
            sol_List.append(item)
            print(item)#and item in not 
        #print(item,type(item))

    print("final sol is :",sol_List.pop(0),sol_List.pop())

findSubString("aqwzbcdefu")

inputStr="aqwzbcdefu"
for item in inputStr:
    print (item)