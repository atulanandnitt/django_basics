# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:02:28 2018

@author: atul
"""

#practice listNode: is it circular ?

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.root=None

    def addData(self,val):
        if self.root ==None:
            self.root = Node(val)
        
        else:
            temp =self.root
            
            while 1:
                if temp.next:
                    temp = temp.next
                else:
                    temp.next=Node(val)
                    break
                
    def disp(self):
        temp = self.root
        while 1:
            if temp:
                print(temp.data)
                temp= temp.next
            else:
                break
    """
    def lenOfLinkedList(self):
        length =0
        temp = self.root
        
        while 1:
            if temp.next:
                temp =temp.next
                length +=1
            else:
                break
        return length
            
    def checkCircular(self):
        temp1= self.root
        temp2= self.root
        count =0
        
        while 1:
            temp1=temp1.next
            temp2=temp2.next #.next
            
            if temp1 ==temp2:
                print("Linkedlist is circular")
                break
            count +=1
            
            if count == self.lenOfLinkedList() -2:
                print("Linkedlist is NOT circular")
                break
                
                
        
    def makeLinkedListCircular(self):
        temp = self.root
        
        while 1:
            if temp.next:
                temp= temp.next
        
        temp.next = self.root
    """
    
    def reverse(self):
        temp = self.root
        p=self.root
        q= temp.next
        r = q.next
        print(r,type(r))
        print("reverse")
        p.next = None
        while 1:
            q.next=p
            p=q
            q=r
            #print(r,type(r))
            if r.next:
                r=r.next
            
            if q.next == None:
                q.next=p
                self.root=q
                break
         
                
     
linkedlist =  LinkedList()

for item in range(1,11):
    linkedlist.addData(item)           
            
linkedlist.disp()    
#linkedlist.checkCircular() 

linkedlist.reverse()
linkedlist.disp() 


import pandas as pd
pd.open("input.txt","r")
df = pd.read()
print(df)
