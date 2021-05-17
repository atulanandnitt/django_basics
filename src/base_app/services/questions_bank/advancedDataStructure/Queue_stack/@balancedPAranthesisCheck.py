

#balanced Paranthesis check: ???????????

def balance_check(s):
    
    if len(s) %2 !=0:
        return False
    
    opening = set('({[')
    
    matches = set([ ('(' ,')') ,('[',']') , ('{','}') ])
    
    stack =[]
    
    for paren in s:
        
        if paren in opening:
            stack.append(paren)
        
    else:
        if len(stack) ==0:
            return False
        
        last_open = stack.pop()
        
        if (last_open,paren) not in matches:
            return False
        
    return len(stack) ==0
        

inputStr='({[]})'
print(balance_check(inputStr))

print(balance_check('{()}'))
result=balance_check("{()[]}({)}")










# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:24:14 2018

@author: atul
"""

#balanced Paranthesis check

def closer(bracket):
    if (bracket == '('):
        return ')'
    elif (bracket =='{'):
        return '}'
    else:
        return ']'
    
def checkBalancedParanthesis(inputStr):
    openings=set('({[')#openings=set("(",'{','[')
    closing=set(')}]')
    
    print(openings,"closing: ", closing)
    stack1=[]
    print(len(inputStr))
    #stack1.append(inputStr[0])
    
    for item in inputStr:
        print(item)
    if len(inputStr) %2 == 1:
        return False
    
    else:
        for item in inputStr:
           if item in closing:
                print("stack1 :",stack1,"   len(stack1) : ",len(stack1))
                if item  == closer(stack1[len(stack1)-1]):
                    stack1.pop()
                    print("after poping : ",stack1)
                else:
                    stack1.append(item)
                    print(stack1)
           else:
                stack1.append(item)
                print(stack1)
                    
    if len(stack1) ==0:
        return True
    else:
        return False
                        
    
                
            
            
            
inputStr="(){}{}"
"""
i=0
inputList=[2,3,44,67,78,7,45,45]
for item in inputList:
    i+=1
    print(inputList.pop())
    
print(inputList)    
print(i)
"""



result=checkBalancedParanthesis("{()[]}({)}")
print(result)