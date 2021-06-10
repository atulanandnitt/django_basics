# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:35:44 2018

@author: Atul Anand
"""

class Node:
    
    def __init__(self,val):
        self.data = val
        self.right =None
        self.left = None
    
class BST:
    
    def __init__(self):
        self.root = None
    
    def createTree(self,val):
        if self.root :
            temp = self.root
            while 1:
                if temp.data < val:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = Node(val)
                        break
                elif val < temp.data:
                    if temp.left :
                        temp=temp.left
                    else:
                        temp.left = Node(val)
                        break
        else:
            self.root= Node(val)
     
    def leftView(self):
        tempLevel=0
        self.root.level =tempLevel
        tempQ=[self.root]
        
        leftViewList=[self.root.data]
        while tempQ:
            temp=tempQ.pop(0)
            
            if temp.level > tempLevel:
                leftViewList.append(temp.data)
                tempLevel = tempLevel +1
                print("temp.data",temp.data)
                print("temp.level",temp.level)
                print("tempLevel",tempLevel)
            
            if temp.left:
                temp.left.level = temp.level +1
                tempQ.append(temp.left)
            if temp.right:
                temp.right.level = temp.level +1
                tempQ.append(temp.right)
            
        print(leftViewList)
        
        
    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
            
    def topView(self):
        print("finding topView")
        self.root.grid=0
        tempQ=[[self.root,self.root.grid]]
        tempGrid=0
        gridAlreadySelected=set()
        topViewList=[]
        print("tempQ data :")
        for item in tempQ:
            print(item[0].data)
            
        while tempQ:
            temp = tempQ.pop(0)
            for item in tempQ:
                print(item[0].data)
            print("finding ",temp[1],"in :",gridAlreadySelected)
            if temp[1] in gridAlreadySelected:
                continue
            else:
                topViewList.append(temp[0].data)
                gridAlreadySelected.add(temp[1])
            
            if temp[0].left:
                temp[0].left.grid = temp[0].grid - 1
                tempQ.append([temp[0].left,temp[0].left.grid])
            
            if temp[0].right:
                temp[0].right.grid = temp[0].grid +1
                tempQ.append([temp[0].right, temp[0].right.grid])
        
        print(topViewList)
            
    def isSatisfyConditions(self,temp):
        if temp.left and temp.right:
            if temp.left.data < temp.data and temp.data < temp.right.data:
                return True
            else:
                return False
        elif temp.left:
            if temp.left.data < temp.data:
                return True
            else:
                return False
        elif temp.right:
            if temp.data < temp.right.data:
                return True
            else:
                return False
        
        
    def isBST(self,temp):
        tempLevel=0
        self.root.level =tempLevel
        tempQ=[self.root]
        self.root.right = Node(1.1)
        levelOrderList=[self.root.data]
        while tempQ:
            temp=tempQ.pop(0)
            
            if temp.level > tempLevel:
                levelOrderList.append("\n")
                tempLevel = tempLevel +1
            
            levelOrderList.append(temp.data)
            if self.isSatisfyConditions(temp):
                continue
            else:
                return False
            
            if temp.left:
                temp.left.level = temp.level +1
                tempQ.append(temp.left)
            if temp.right:
                temp.right.level = temp.level +1
                tempQ.append(temp.right)
            
        print("Tree is BST")
        return True

    def height(self,temp):
        if temp == None:
            return 0
        else:
            return max(self.height(temp.left) , self.height(temp.right)) +1

    def size(self,temp):
        if temp == None:
            return 0
        else:
            return (self.size(temp.left) + self.size(temp.right)) +1
        
    def getSize(self,temp):
        if temp:
            return 1+ self.getSize(temp.left) + self.getSize(temp.right)
        else:
            return 0
        
        
bst=BST()

list1=[5,3,1,2,4,4.5,4.7,4.9]

for item in list1:
    bst.createTree(item)
    
bst.inorder(bst.root)
bst.leftView()   
print("*****************************************") 
bst.topView()
print(bst.isBST(bst.root))
print(bst.height(bst.root))
print(bst.size(bst.root))
print(bst.getSize(bst.root))