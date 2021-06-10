# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 13:46:45 2018

@author: atul
"""
#bst

class Node:
    def __init__(self,val):
        self.data=val
        self.left = None
        self.right=None
    
    def __str__(self):
        return str(self.data)
    
    
    
class Tree():
    def __init__(self):
        self.root =None
        
    def create(self,val):
        if self.root == None:        
            self.root = Node(val)
        
        else:
            tempNode = self.root
            
            while 1:
                    
                if val < tempNode.data:
                    if tempNode.left:
                        tempNode = tempNode.left
                    else:
                        tempNode.left = Node(val)
                        break
                
                if tempNode.data < val :
                    if tempNode.right:
                        tempNode = tempNode.right
                    else:
                        tempNode.right = Node(val)
                        break


    def postOrder(self,tempNode):
        if tempNode:
            self.postOrder(tempNode.left)
            self.postOrder(tempNode.right)
            print(tempNode.data)





    def preorder(self,tempNode):
        if tempNode is not None:
            print(tempNode.data)
            self.preorder(tempNode.left)
            self.preorder(tempNode.right)
                    
    def inorder(self,tempNode):
        if tempNode is not None:
            self.inorder(tempNode.left)
            print(str(tempNode.data))
            self.inorder(tempNode.right)
            
            
tree = Tree()
item =[5,4,6,3,7,2,8,1,9]

for items in item:
    tree.create(items)

tree.inorder(tree.root)
print("preorder")
tree.preorder(tree.root)

print('postorder')
tree.postOrder(tree.root)