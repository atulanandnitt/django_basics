# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:43:19 2018

@author: atul
"""

#Queue using 2 Stack

class Stack:
    def __init__(self):
        self.items=[]
    
    
    def push(self,val):
        self.items.append(val)
        
    def isEmpty(self):
        return self.items ==[]
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.items.pop()
    
    def length(self):
        return len(self.items)
    

    
    
s1=Stack()
s2=Stack()

#enque: to push in Queue
for i in range(11):
    s1.push(i)
    
#to dequeu
def deque(s1):
    for i in range(s1.length() -1):
        #print("poped and enqued in S1")
        s2.push(s1.pop())
    
    sol=s1.pop()
    
    while s2.length()>0:
        s1.push(s2.pop())    
        
    return sol

itemDequed=deque(s1)
print(itemDequed)

itemDequed=deque(s1)
print(itemDequed)







print("AS per the solution in internet")

class Queeu2Stacks(object):
    def __init__self(self):
        self.instack=[]
        self.outstack=[]
        
    def enqueue(self,val):
        self.instack.append(val)
       
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()
    """
    def dequeue(self):
        while len(self.instack) >1:
            self.outstack.append(self.instack.pop())
        sol=self.instack.pop()
        while len(self.outstack) >0:
            self.instack.append(self.outstack.pop())       
        
        return sol
    """



print("test ur sol")

q= Queeu2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())    
