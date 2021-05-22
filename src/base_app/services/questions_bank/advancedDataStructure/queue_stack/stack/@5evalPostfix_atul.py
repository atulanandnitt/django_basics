# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:21:07 2018

@author: atanand
"""

def doMath(op,a,b):
    if op =='*':
        return a *b
    elif op =='/':
        return a/b
    elif op == '+':
        return a+b
    elif op =='-':
        return a-b
        
        
        
def evalPostFixOperation(list1):
    stack=[]
    num={0,1,2,3,4,5,6,7,8,9}
    for item in list1:
        if item in num:
            stack.append(item)
        else:
            a=stack.pop()
            b=stack.pop()
            sol=doMath(item,a,b)
            stack.append(sol)
    
    print(stack.pop())

list1=[5,6,'*']            
evalPostFixOperation(list1)

list1=[5,6,'+']            
evalPostFixOperation(list1)
        