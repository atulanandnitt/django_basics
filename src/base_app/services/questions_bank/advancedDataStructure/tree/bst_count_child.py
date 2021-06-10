# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:07:46 2018

@author: atul
"""

#count child of each nodes while travesing bfs

class Node :
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root=None
        
    def createTree(self,val):
        if self.root is None:
            self.root = Node(val)
        
        else:
            temp =self.root
            
            while 1:
                if val < temp.data:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left= Node(val)
                        break
                if temp.data < val:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right=Node(val)
                        break
    
    def bfs(self):
        self.root.level=0
        self.root.childCount=0
        temp_level=self.root.level
        childCount=self.root.childCount
        tempList=[self.root]
        solList=[]
        childCountList=[]
        
        while len(tempList) >0:
            temp=tempList.pop(0)
            
            if temp.level > temp_level:
                temp_level +=1
                solList.append('\n')
            
            solList.append(temp.data)
            
            if temp.left:
                temp.left.level=temp_level+1
                tempList.append(temp.left)
                temp.childCount +=1
            
            if temp.right:
                temp.right.level=temp_level+1
                tempList.append(temp.right)
                temp.childCount +=1
            
            childCountList.append(temp.childCount)
            print(temp.childCount)
                
        print(solList)   
                     
        
        
        
    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
            
arr=[5,4,6,3,7,2,8,1,9]
bst = Tree()
for item in arr:
    bst.createTree(item)
    
bst.inorder(bst.root)    
        
bst.bfs()
        