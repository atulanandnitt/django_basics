# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:46:45 2018

@author: atanand
"""

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
class Tree:
    def __init__(self):
        self.root=None        
    
    def createTree(self,val):
        if self.root == None:
            self.root = Node(val)
            
        else:
            temp=self.root
            
            while 1:
                if temp.data > val:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=Node(val)
                        break
                if temp.data < val:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=Node(val)
                        break
                else:
                    continue
    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
            
    def findMaxElem(self,temp):
        temp=self.root
        while temp.right:
            temp=temp.right
        return temp.data

    def findMinElem(self,temp):
        temp=self.root
        while temp.left:
            temp=temp.left
        return temp.data
    
    def sizeOfTree(self,temp):
        if temp.left and temp.right:
            return self.sizeOfTree(temp.left) + self.sizeOfTree(temp.right) +1
        elif temp.left:
            return self.sizeOfTree(temp.left)+1
        elif temp.right:
            return self.sizeOfTree(temp.right)+1
        else:
            return 1
            
    def heightOfTree():#maxDepth
        if temp.left is not None and temp.right is not None:
            return max(self.findDeepesetNode(temp.left),self.findDeepesetNode(temp.right)) +1
        elif temp.left:
            return self.findDeepesetNode(temp.left) +1
            
        elif temp.right:
            return self.findDeepesetNode(temp.right) +1
           
        else:
            return 1
        
    def findDeepesetNode(self,temp):
        self.root.level=0
        temp_level=self.root.level
        temp_list=[self.root]
        bfs_list=[]
        
        while len(temp_list) >0:
            
            temp=temp_list.pop(0)
            
            if temp.level > temp_level:
                temp_level +=1
                bfs_list.append('\n')
            
            bfs_list.append(temp.data)
            
            if temp.left:
                temp.left.level = temp_level+1
                temp_list.append(temp.left)
        
            if temp.right:
                temp.right.level = temp_level+1        
                temp_list.append(temp.right)
                
        print("bfs_list")
        for item in bfs_list:
            print(item)
        
        return bfs_list.pop()
    
    counterFullNode=0
    counterHalfNode=0
    def countHalfNodes(self,temp):#can be done through any traversal technic: inorder,pre,post,bfs: here I am doing by inorder
        if temp:
            self.countHalfNodes(temp.left)
            if temp.left and temp.right:
                counterFullNode +=1
            elif temp.left or temp.right:
                counterHalfNode +=1
            self.counterHalfNodes(temp.right)
        print( counterHalfNode,counterFullNode)
    
    def countHalfNodes_bfs(self,temp):#can be done through any traversal technic: inorder,pre,post,bfs: here I am doing by bfs
        print("countHalfNodes_bfs")
        fullNode=[]
        halfNode=[]
        self.root.level=0
        temp_level=self.root.level
        temp_list=[self.root]
        bfs_list=[]
        leaf=[]
        while len(temp_list)>0:
            temp=temp_list.pop(0)
            
            if temp.level > temp_level:
                temp_level +=1
                bfs_list.append('\n')
            
            if temp.left and temp.right:
                fullNode.append(temp.data)
            
            elif temp.left and temp.right is None:#can we place elif in between many if condition
                halfNode.append(temp.data)
            elif temp.left is None and temp.right:
                halfNode.append(temp.data)
            elif temp.left is None and temp.right is None:
                leaf.append(temp.data)
                
            bfs_list.append(temp.data)
            
            if temp.left:
                temp.left.level = temp.level +1
                temp_list.append(temp.left)
            if temp.right:
                temp.right.level = temp.level +1
                temp_list.append(temp.right)
                
        print("halfNode :",halfNode)
        print("fullNode : ",fullNode)
        print( "counterHalfNode :",len(halfNode),"counterFullNode : ",len(fullNode))
        print("leaf",leaf)

    counterFullNode=0
    counterHalfNode=0
    def compareTwoTrees(self,temp1,temp2):#can be done through any traversal technic: inorder,pre,post,bfs: here I am doing by inorder
        if temp:
            self.countHalfNodes(temp.left).val == self.countHalfNodes(temp.left).val 
            if temp.left and temp.right:
                counterFullNode +=1
            elif temp.left or temp.right:
                counterHalfNode +=1
            self.counterHalfNodes(temp.right)
        print( counterHalfNode,counterFullNode)
    
    def check_is_bianryTree(self,temp):
        if temp:
            if self.root and self.root.val > temp.left.val:
                return False
            
            if self.root and self.root.val < temp.right.val:
                return False
            
            if not self.check_is_bianryTree(self.root.left) or not self.check_is_bianryTree(self.root.right):
                return False
        else:
            return True
    
    ptr=0
    def diaTree(self,temp):
        global ptr
        if temp is None:
            return 0
        left = self.diaTree(temp.left)
        right = self.diaTree(temp.right)
        
        if left + right > ptr:
            ptr = left + right
        return max(left,right) +1
    
        
        
def compare2Tree(t1,t2):
    print("compare2Tree")
    flag= False
    #root1=t1.root
    #root2=t2.root
    #print(root1.data)
    #print(root2.data)
    t1.root.level=0
    t2.root.level=0
    temp_level1=t1.root.level
    temp_level2=t2.root.level
    temp_list1=[t1.root]
    temp_list2=[t2.root]
    bfs1=[]
    bfs2=[]
    
    print("temp_list1.data   ::::  ",temp_list1.pop().data)
    while len(temp_list1) > 0 or len(temp_list2) >0:
        if len(temp_list1) != len(temp_list2):
            return False
        
        try:
                
            temp1=temp_list1.pop(0)
            temp2=temp_list2.pop(0)
            print('temp1 : ',temp1.data,"temp2 : ",temp2.data)
        except:
            print("encountered execption")
            return flag
        
        if temp1.level > temp_level1:
            temp_level1 +=1
            bfs1.append(temp1.data)
            
        if temp2.level > temp_level2:
            temp_level2 +=1
            bfs2.append(temp2.data)
        
        bfs1.append(temp1.data)
        bfs2.append(temp2.data)
        
        print("temp1.data : ",temp1.data,"temp2.data : ",temp2.data)
        if temp1.data is not temp2.data:
            return flag
        
        if temp1.left:
            temp1.left.level = temp1.level + 1
            temp_list1.append(temp1.left)
        
        if temp1.right:
            temp1.right.level = temp1.level + 1
            temp_list1.append(temp1.right)
            
        if temp2.left:
            temp2.left.level = temp2.level + 1
            temp_list2.append(temp2.left)
            
        if temp2.right:
            temp2.right.level = temp2.level + 1
            temp_list2.append(temp2.right)        
        
        
    return True


    
bst=Tree()    
list1=[6,5,7,4,8,3,9,2,10,11,111,1,0,-1,-2]
for item in list1:
    bst.createTree(item)

bst2=Tree()    
list1=[6,5,7,4,8,3,9,2,10,11,111,1,0,-1,-2]
for item in list1:
    bst2.createTree(item)
    
print("compare2Tree(bst,bst2)",compare2Tree(bst,bst2) )
if compare2Tree(bst,bst2):
    print("both trees are identical")
else:
    print("both trees are NOT identical")

"""  
print("bst.findMaxElem(bst.root) : ",bst.findMaxElem(bst.root))

print("bst.findMinElem(bst.root) : ",bst.findMinElem(bst.root)) 

print("bst.findDeepesetNode(bst.root)",bst.findDeepesetNode(bst.root))

print("bst.sizeOfTree(bst.root)",bst.sizeOfTree(bst.root))       

#counterHalfNode,counterFullNode=bst.countHalfNodes_bfs(bst.root)

bst.countHalfNodes_bfs(bst.root)

print("bst.diaTree(bst.root)",bst.diaTree(bst.root))
"""