# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:23:01 2018

@author: atanand
"""

class HashTable:
    
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    
    def put1(self,key,data):
        
        hashvalue = self.hashfunction(key,len(self.slots))
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] =data
                
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                    
                if self.slots[nextslot] == None:
                    self.slots[nextslot] =key
                    self.data[nextslot] =data
                
                else:
                    self.data[nextslot] = data
                    
    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash +1)%size
    
    def get1(self,key):
        
        startslot = self.hashfunction(key,len(self.slots))
        data =None
        stop =False
        found = False
        position = startslot
        
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            
            else:
                position = self.rehash(position,len(self.slots))
                
                if position == startslot:
                    stop =True
        return data
    
    def __getitem__(self,key):
        print("inside __getitem__" )
        return self.get1(key)
    
    def __setitem__(self,key,data):
        print("inside __setitem__" )
        self.put1(key,data)


h = HashTable(5)

h[1]='one'
h[2]='two'

for i in range(1,3):
    print(h[i])        