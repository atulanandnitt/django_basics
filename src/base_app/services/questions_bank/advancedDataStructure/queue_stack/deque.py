# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:26:51 2018

@author: atul
"""

#deque

class Deque:
    maxSize =10
    
    def __init__(self):
        self.items=[]
    
    def isFull(self):#say maxSize
        if len(self.items) >= 10:
            return True
        else:
            return False
        
    def isEmpty(self):
        return self.items ==[]
        
        
    def insertAtFront(self,val):
        if self.isFull():
            return
        else:
            self.items.insert(0,val)
    
    def insertAtEnd(self,val):
        if self.isFull():
            return
        else:
            self.items.append(val)
            
    def popFromFront(self):
        if self.isEmpty():
            return "isEmpty deque, pop cant be opeerated"
        else:
            return self.items.pop(0)
            

    def popFromEnd(self):
        if self.isEmpty():
            return "isEmpty deque, pop cant be opeerated"
        else:
            return self.items.pop() 

deque2 = Deque()
for item in range(11):
    print("inserted emement is ",item)
    deque2.insertAtEnd(item)


for item in range(11):
    print(deque2.popFromEnd())
    
    

for item in range(11):
    deque2.insertAtEnd(item)


for item in range(11):
    print(deque2.popFromFront())
    
    
for item in range(11):
    deque2.insertAtFront(item)


for item in range(11):
    print(deque2.popFromFront())    
    

for item in range(11):
    deque2.insertAtEnd(item)


for item in range(11):
    print(deque2.popFromFront())    
    
for item in range(11):
    deque2.insertAtEnd(item)


for item in range(11):
    print(deque2.popFromFront())        