# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:58:27 2018

@author: atul
"""

class Queue:
    def __init__(self):
        self.data =[]
        
    def isEmpty(self):
        return len(self.data) ==0
    
    def enqueue(self,val):
        self.data.insert(0,val)
        return val
        
    def dequeue(self):
        try:
            a=self.data.pop()
            return a
        except: 
            print("queue is empty so dequeue cant be performed")
    
    #def isFull(self): ??

q = Queue()

for i in range(11):
    q.enqueue(i)    


print(q.isEmpty())
print(q.dequeue()) 

print("value in q is : ",q.data)
for i in range(15):
    print(q.dequeue())        
    
for i in range(15):
    print(q.enqueue(i))   
  
for i in range(22):
    print(q.dequeue()) 
    
    
"""
#priority Queue
print("create a normal queue")

class CreateQueue:
    
    maxLength =10
    front,end=-1,-1
    q=[]
        
    
    def queueIsFull(self):
        if len(q) == maxLength:
            return True
        else:
            return False
        
    def queueIsEmpty(self):
        if front == end:
            return True
        else:
            return False
    
    def enqueue(self,val):
        if queueIsFull():
            print ("Queue is full so no new element will be added")
            return
        else:
            front =0
            end +=1
            q.append(val)
        
    def dequeue(self):
        if queueisEmpty():
            return
        else:
            q.pop()
"""            