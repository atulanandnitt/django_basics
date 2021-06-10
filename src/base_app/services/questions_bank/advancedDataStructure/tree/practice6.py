# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 11:57:28 2018

@author: atul
"""

class Node:
    def __init__(self,val):
        self.data= val
        self.left=None
        self.right=None
    
class Tree:
    def __init__(self):
        self.root=None
    
    def createTree(self,val):
        if self.root is None:
            self.root = Node(val)
            print("added node for root",val)
        else:
            temp=self.root
            
            while 1:
                #print("creating bst")
                if val < temp.data:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=Node(val)
                        #print("added node for left",val,"temp data is",temp.data)
                        break
                elif val > temp.data:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=Node(val)
                        #print("added node for right",val,"temp data is",temp.data)
                        break
                else:
                    break
    
    def bfs(self):
        self.root.level=0
        temp_level=self.root.level
        tempList=[self.root]
        result=[]
        leftView=[]
        leftView.append(self.root.data)
        #rightView.append(self.root.data)
        while len(tempList) >0:
            
            temp=tempList.pop(0)
            
            if temp_level < temp.level:
                temp_level+=1
                result.append('\n')
                leftView.append(temp.data)
                #print("level changed at  ",temp.data)
            
            result.append(temp.data)
            
            if temp.left:
                temp.left.level=temp_level+1
                tempList.append(temp.left)
            
            if temp.right:
                temp.right.level=temp_level+1
                tempList.append(temp.right)
        
        print(result)
        print("leftView",leftView)
        print("sumAt different level")
        result.append('\n')
        sumAtlevel=0
        sumAtlevelList=[]
        for item in result:
            #print(item)
            if item != '\n':
                #print("adding",item)
                sumAtlevel +=item
            else:
                sumAtlevelList.append(sumAtlevel)
                sumAtlevel=0

        rightMostElememtAtThatLevel=self.root.data 
        rightMostElememtList=[]
        #rightMostElememtList.append(rightMostElememtAtThatLevel)
        for item in result:
            if item != '\n':
                rightMostElememtAtThatLevel=item
            else:
                rightMostElememtList.append(rightMostElememtAtThatLevel)        
        print("rightMostElememtList",rightMostElememtList)   

    
    def inorder(self,temp):
        #temp=self.root
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
    
bst =Tree()        
arr = [8,3,1,6,4,7,10,14,13,12,11,15,16,17,18,2,5,9]
for item in arr:
    print(item)
    bst.createTree(item)

print("created bst")    
bst.inorder(bst.root)    
print("printed bst")    
    
bst.bfs()         
        
                    
            