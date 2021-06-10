# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:17:06 2018

@author: atul
"""

#queue

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items ==[]
        
        
    def isFull(self):#lets say max size defined as 10
        if len(self.items) >= 10:
            return True
        else:
            return False
        
    def enqueue(self,val):
        if self.isFull() is False:
            self.items.append(val)
        else:
            print("Queue is full")
    
    def dequeue(self):
        if self.isEmpty() is False:
            return self.items.pop(0)
        else:
            return "Queue is Empty"
    
q1=Queue()

for item in range(10):
    q1.enqueue(item)

for item in range(10):
    print(q1.dequeue())