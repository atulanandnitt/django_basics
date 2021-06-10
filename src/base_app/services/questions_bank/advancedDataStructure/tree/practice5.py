# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:21:39 2018

@author: atul
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:49:38 2018

@author: atul
"""

#tree
#practice Bft

class Node:
    def __init__(self,val):
        self.data = val
        self.left=None
        self.right=None
        
    def __str__(self):
        return str(self.data)
    
    
class Tree:
    def __init__(self):
        self.root= None
    
    def create(self,val):
        if self.root == None:
            self.root =Node(val)
        else:
            temp = self.root
            
            while 1:
                if temp.data >val:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=Node(val)
                        break
                elif temp.data <val:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right=Node(val)
                        break
                else:
                    break

    def max(leftDepth,rightDepth):
        if leftDepth> rightDepth:
            return leftDepth
        else:
            return rightDepth
    
    def getHeight(self,tempNode):
        if tempNode.left and tempNode.right:
            return 1+max(self.getHeight(tempNode.left),self.getHeight(tempNode.right))
        elif tempNode.right:
            return 1+self.getHeight(tempNode.right)
        elif tempNode.left:
            return 1+self.getHeight(tempNode.left)
        else:
            return 1
#max depth
    def bft(self):
        self.root.level=0
        temp_level= self.root.level
        queue=[self.root]
        out=[]
        print("queue &&&&&&&&&&&&&&&&&&&&&&&&&& ",queue)
        
        while len(queue) >0:
            
            #print("queue ******************",queue)
            for item in queue:
                print("queue items are ",item)
            temp_node= queue.pop(0)
            print("temp_node {},temp_node.level{} ".format(temp_node,temp_node.level))
            #print(" temp_node.level******************",temp_node.level)
            print( "temp_level ***********************",temp_level)
            
            
            if temp_node.level > temp_level:
                temp_level +=1
                out.append('\n')
              
         
            out.append((temp_node.data))
            
            #print(out)
            
            if temp_node.left:
                temp_node.left.level = temp_level+1
                
                queue.append(temp_node.left)
            
            if temp_node.right:
                temp_node.right.level = temp_level+1
                
                queue.append(temp_node.right)
        print(out)  

        
    
    def inorder(self,node):
            
           if node is not None:
              
              self.inorder(node.left)
              print (str(node))
              self.inorder(node.right)

    def mirrorImageInorder(self,node):
        if node:
            self.mirrorImageInorder(node.right)
            print(str(node))
            self.mirrorImageInorder(node.left)

    def preorder(self,node):
            
           if node is not None:
              
              print (node.data)
              self.preorder(node.left)
              self.preorder(node.right)


    def postorder(self,node):
            
           if node is not None:
              
              self.postorder(node.left)
              self.postorder(node.right)
              print (node.data)

                        
tree = Tree()     
arr = [8,3,1,6,4,7,10,14,13,12,11,15,16,17,18]
for i in arr:
    tree.create(i)
print ('Breadth-First Traversal')
tree.bft()
"""
print ('Inorder Traversal')
tree.inorder(tree.root) 
print ('Preorder Traversal')
tree.preorder(tree.root) 
print ('Postorder Traversal')
tree.postorder(tree.root)
print ('mirrorImageInorder')
tree.mirrorImageInorder(tree.root)
print("getHeight", tree.getHeight(tree.root))
"""