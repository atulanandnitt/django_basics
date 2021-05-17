# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:45:09 2018

@author: atul
"""

#bst

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.data)
    

class Tree:
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        print("inserting ************ ",item)
        if self.root is None:
            self.root = Node(val)
        
        else:
            temp=self.root
            
            while 1:
                if val < temp.data:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=Node(val)
                        break
                elif val > temp.data:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=Node(val)
                        break
                else:
                    break

    def bfs(self):
        self.root.level=0
        temp_level=self.root.level
        temp_list=[self.root]
        result=[]
        leftView,rightView=[] ,[]
        leftView.append(self.root.data)
        #rightView.append(self.root.data)
        
        while len(temp_list)>0:
            temp=temp_list.pop(0)
            
            if temp_level < temp.level:
                temp_level +=1
                leftView.append(temp.data)
                result.append('\n')
            
            result.append(temp.data)
            
            if temp.left:
                temp.left.level=temp_level+1
                temp_list.append(temp.left)
            
            if temp.right:
                temp.right.level = temp_level+1
                temp_list.append(temp.right)
            
        print("result of bfs",result)
        print("left view",leftView)
        
        prevItem=0
        for item in result:
            if item is '\n':
                rightView.append(prevItem)
                
            else:
                prevItem=item
        print(rightView)      
        
    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
            
array = [8,3,1,6,4,7,10,14,13,12,11,15,16,17,18,2,5,9]
bst =Tree()
for item in array:
    print(item)
    bst.insert(item)                

bst.inorder(bst.root)

bst.bfs()
