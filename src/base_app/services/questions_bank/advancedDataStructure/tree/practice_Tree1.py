#tree

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root =None
    
    def createTree(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            temp=self.root
            print("val of temp",val)
            while 1:
                if temp.data > val:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=Node(val)
                        break
                elif temp.data < val:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right = Node(val)
                        break
                else:
                    pass
    def inorderRec(self,temp):
        if temp:
            self.inorderRec(temp.left)
            print(temp.data)
            self.inorderRec(temp.right)
        
    def bfs(self):
        tempList=[self.root]
        self.root.level=0
        tempLevel=self.root.level
        bfsList=[]
        leftView=[self.root.data]
        while tempList:
            
            temp=tempList.pop(0)
            
            if temp.level > tempLevel:
                tempLevel +=1
                bfsList.append("\n")
                leftView.append(temp.data)
            
            bfsList.append(temp.data)
            #print(" bfsList is : " ,bfsList)
            if temp.left:
                temp.left.level = temp.level +1
                tempList.append(temp.left)
                #print(temp.left.data ," inserted ")
            
            if temp.right:
                temp.right.level = temp.level +1
                tempList.append(temp.right)
                #print(temp.right.data ," inserted ")
                
        print(bfsList)
        print("leftView ",leftView)
    
    
   

    def rightView(self):
        self.root.level=0
        tempList=[self.root]
        tempLevel=self.root.level
        rightViewList=[self.root.data]
        
        while tempList:
             temp =tempList.pop(0)
             
             if temp.level > tempLevel:
                 tempLevel +=1
                 rightViewList.append(temp.data)

  
             if temp.right:
                    temp.right.level =temp.level+1
                    tempList.append(temp.right)
                                    
             if temp.left:
                    temp.left.level = temp.level+1
                    tempList.append(temp.left)
                     
          
        print("rightViewList",rightViewList)    
        
    def getHeight(self,temp):
        if temp:
            return 1 + max(self.getHeight(temp.left) ,self.getHeight(temp.right))
        else:
            return 0
    
    def getSize(self,temp):
        if temp:
            return 1+ self.getSize(temp.left) + self.getSize(temp.right)
        return 0
    
    def mirror(self,temp):
        if temp:
            self.mirror(temp.right)
            print(temp.data)
            self.mirror(temp.left)
    
    def maxSumAtWhatLevel(self):
        tempList=[self.root]
        self.root.level=0
        tempLevel=self.root.level
        tempMax=0
        sumAtLevel=0
        maxAtLevel=0
        #tempListAtCurrentLevel=[]
        while tempList:
            temp=tempList.pop(0)
            
            if temp.level > tempLevel:
                if sumAtLevel > tempMax:
                    tempMax = sumAtLevel
                    maxAtLevel = tempLevel
                tempLevel += 1
                sumAtLevel=0
                
            sumAtLevel += temp.data
            
            if temp.left:
                temp.left.level=temp.level+1
                tempList.append(temp.left)
                
            if temp.right:
                temp.right.level=temp.level +1
                tempList.append(temp.right)
            
        print("maxAtLevel : ",maxAtLevel, "Max sum is :",tempMax )
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
bst=Tree()
list1=[5,4,63,7,2,8,1,9,0,-1,91]
for item in list1:
    bst.createTree(item)
    
print("inorder tree inorderRec :")    
bst.inorderRec(bst.root)    
print("bfs  : ")
bst.bfs()


print("rightView")
bst.rightView()

print("height")
print(bst.getHeight(bst.root))
print("Size ")
print(bst.getSize(bst.root))

print("miror of inorder")
bst.mirror(bst.root)


bst.maxSumAtWhatLevel()