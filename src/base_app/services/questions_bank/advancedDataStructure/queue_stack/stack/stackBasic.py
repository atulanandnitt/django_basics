# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 06:21:01 2018

@author: atanand
"""

class Stack(object):
#class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        
        if len(self.items) ==0:
            return True
        else:
            return False
        
        #return self.items ==[]
        
    def isFull(self):
        if len(self.items) <10:#max size of a Stack can be specified
            return False
        return True
    
    def push(self,val):
        #self.items.append(val)
        
        if self.isFull() == False:
            self.items.append(val)
            print(val,"is inserted")
        else:
            print("Stack is full")
        
    # how to call a function from the same class
    def pop(self):
            return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items) - 1 ]

s1=Stack()  


for item in range(10):
    s1.push(item)

for item in range(10):
    print(s1.pop())
    
    
    
print(s1.isEmpty())      
s1.push('a')
s1.push('b')
s1.push('c')
s1.push('d')
s1.push(1)
s1.push("atul")
s1.push('a')
s1.push('b')
s1.push('c')
s1.push('d')
s1.push(1)
s1.push("atul")
s1.push('a')
s1.push('b')
s1.push('c')
s1.push('d')
s1.push(1)
s1.push("atul")

print(s1.pop())



