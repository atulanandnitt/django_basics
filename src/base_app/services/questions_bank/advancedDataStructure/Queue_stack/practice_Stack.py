# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 07:38:16 2018

@author: atanand
"""

#stack

class Stack:
    def __init__(self):
        self.items=[]
        top=0
        bottom=0
    
    def isFull(self):
        return False
    
    def isEmpty(self):
        return self.items ==[]
    
    def push(self,val):
        if self.isFull():
            return
        else:
            self.items.append(val)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty, pop operation can't be used")
        else:
            return self.items.pop()
    
    def top(self):
        if self.isEmpty():
            print("Stack is empty, top operation can't be used")
        else:
            return self.items[len(self.items) -1]
        
     
s1=Stack()
s1.push('a')
s1.push('b')
s1.push('a')
s1.push('b')

for i in range(4):
    print(s1.top())