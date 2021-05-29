# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 09:49:20 2018

@author: atul
"""

#reversal of str:

def strReversalCharByChar(input_str):
    i=0
    length=len(input_str)
    print("length",length)
    #inputList=input_str.strip().split()
    sol_str=""
    sol_list=[]
    while i < length:
        sol_list.append(input_str[length -1 -i])
        i +=1
    #print(sol_list) 
    sol_str="".join(sol_list)
    return (sol_str)
    


input_str="My name is Atul"
print("input_str : ",input_str)
sol=strReversalCharByChar(input_str) 
print(sol)

def strReversalWordByWord(input_str):
    print("strReversalWordByWord")
    inputList= input_str.strip().split(" ")
    sol=[]
    for item in inputList:
        sol.append(strReversalCharByChar(item))
        sol.append(" ")
        
        #print(item)
    print("".join(sol))

strReversalWordByWord(input_str)        
