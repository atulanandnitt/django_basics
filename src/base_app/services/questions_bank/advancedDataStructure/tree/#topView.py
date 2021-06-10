# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 12:44:58 2018

@author: atanand
"""

#adobe face-2-face round

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        

class Tree:#not a bst
    def __init__(self):
        self.root=None
        
    def createNormalTree(self,val):
        if self.root == None:
            self.root=Node(val)
            print("root is : ",self.root.data)
        
        else:
            temp=self.root
            while 1:
                if temp.left == None and temp.right == None:
                    temp.left = Node(val)
                    print("inserted element in left side is ",val)
                    break
                elif temp.left is not None and temp.right == None:
                    temp.right=Node(val)
                    temp=temp.right
                    print("inserted element in right side is:  ",val)
                    break
                elif temp.left == None and temp.right is not None:
                    temp=temp.left
                elif temp.left is not None and temp.right is not None:
                    if temp.left.left is not None and temp.left.right is not None:
                        if temp.right.left is not None and temp.right.right is not None:
                            temp=temp.left
                        else:
                            temp=temp.right
                    else:
                        temp=temp.left
    
    def createBst(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            temp = self.root
            
            while 1:
                if temp.data >val:   
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=Node(val)
                        break
                
                elif temp.data<val:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=Node(val)
                        break
                else:
                    continue#to avoid repeatation of element in bst even if element is repeated in the input list
        
    def inorder(self,tempNode):
        if tempNode:
            self.inorder(tempNode.left)
            print(tempNode.data)
            self.inorder(tempNode.right)
            
    def topViewTree(self):
        temp=self.root
        topview=[]
        #topview.append(temp.data)
        while temp.left:
            try:
                topview.append(temp.data)
                temp=temp.left
            except:
                print("no left child")
                break
        topview.append(temp.data)
        
        temp2=self.root
        while temp2.right:
            try:
                topview.append(temp2.data)
                temp2=temp2.right
            except:
                print("no right child")
                break
        topview.pop(0)
        topview.append(temp2.data)
        print(topview)    
        
    
genericTree=Tree()
for i in range(10):
    genericTree.createBst(i)
    
genericTree.inorder(genericTree.root)    

genericTree.topViewTree()