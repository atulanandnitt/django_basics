

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
    
    
    
    def bfs_better(self):
        if self.root is None:
            return
        q = [self.root]
        temp = q.pop()
        while temp:
            print(temp.data, ", ", end="")
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
            
            if len(q) > 0:
                temp = q.pop(0)
            else:
                break

    def leftView_better(self):
        q1 = [self.root]
        q2 = list()
        while 1:
            # import ipdb; ipdb.set_trace()
            if len(q2) == 0:
                if len(q1) >0:
                    temp = q1.pop(0)
                print(temp.data, ", ", end="")
                while temp:
                    if temp.left: q2.append(temp.left)
                    if temp.right: q2.append(temp.right)
                    if len(q1) > 0:
                        temp = q1.pop()
                    elif len(q1) == 0: 
                        # print(q2)
                        break

            if len(q1) == 0:
                if len(q2) >0:
                    temp = q2.pop(0)
                print(temp.data, ", ", end="")
                while temp:
                    if temp.left: q1.append(temp.left)
                    if temp.right: q1.append(temp.right)
                    if len(q2) >0:
                        temp = q2.pop(0)
                    elif len(q2) == 0: 
                        # print(q1)
                        break
            
            if len(q1) == 0 and len(q2) ==0:
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
        
        print("result",result)
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

    def leftViewOfTree(self):
        self.root.level=0
        temp_level=self.root.level        
        tempList=[self.root]
        leftViewList=[]
        leftViewList.append(self.root.data)
        while len(tempList) >0:
            #print("tempList",tempList,"")
            temp=tempList.pop(0)
            
            if temp.level > temp_level:
                temp_level +=1
                leftViewList.append(temp.data)
            
            if temp.left:
                temp.left.level=temp_level +1
                tempList.append(temp.left)
                
            if temp.right:
                temp.right.level= temp_level +1
                tempList.append(temp.right)
                
        print(leftViewList)
        
    def rightViewOfTree_trickySol(self):
        self.root.level=0
        temp_level=self.root.level        
        tempList=[self.root]
        leftViewList=[]
        leftViewList.append(self.root.data)
        while len(tempList) >0:
            #print("tempList",tempList,"")
            temp=tempList.pop(0)
            
            if temp.level > temp_level:
                temp_level +=1
                leftViewList.append(temp.data)
            
            if temp.right:
                temp.right.level= temp_level +1
                tempList.append(temp.right)
                
            if temp.left:
                temp.left.level=temp_level +1
                tempList.append(temp.left)
                

                
        print(leftViewList)
        
    def breathFirstTravel(self):
        self.root.level=0
        tempList=[self.root]
        tempLevel=self.root.level
        result=[]
        
        while len(tempList)>0:
            
            temp=tempList.pop(0)
            

            if temp.level > tempLevel:
                tempLevel +=1
                result.append('\n')
            
            result.append(temp.data)
            
            if temp.left:
                temp.left.level=tempLevel+1
                tempList.append(temp.left)
                
            if temp.right:
                temp.right.level=tempLevel+1
                tempList.append(temp.right)
        
        print("complete level order Traversal")
        print(result)
        
            
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
             
    
    
    def rightViewOfTree(self):
        self.root.level=0
        tempList=[self.root]
        tempLevel=self.root.level
        rightView=[]
        result=[]
        
        while len(tempList)>0:
            
            temp=tempList.pop(0)
            

            if temp.level > tempLevel:
                tempLevel +=1
                result.append('\n')
            
            result.append(temp.data)
            
            if temp.left:
                temp.left.level=tempLevel+1
                tempList.append(temp.left)
                
            if temp.right:
                temp.right.level=tempLevel+1
                tempList.append(temp.right)
        
        prev = None
        for item in result:
            if prev is None:
                prev=item
                
            if item =='\n':
                rightView.append(prev)
            
            prev=item
            #print("prev item is",prev)
        
        print(rightView)
            
          
    
    
    def findnode(self,temp,val):
        if temp == None:
            return False
        elif temp.data == val:
            return True
        
        if temp.data <val:
            self.findnode(temp.right,val)
        elif temp.data > val:
            self.findnode(temp.left,val)
            

    def is_cousin(self, x: float, y: float) -> bool:
        dq = deque()
        dq.append(self.root)
        temp = {}
        
        while dq:
            row = set()
            
            for _ in range(len(dq)):
                node = dq.pop()
                print("working on current node.data: ",node.data)
                if node.left:
                    if node.left.data == x:
                        temp[x] = node
                        print("temp : ", temp.get(x).data)
                    if node.left.data == y:
                        temp[y] = node
                        print("temp : ", temp.get(y).data)
                    # print("temp : ", temp, type(temp))
                    
                    dq.appendleft(node.left)
                if node.right:
                    if node.right.data == x:
                        temp[x] = node
                        print("temp : ", temp.get(x).data)
                    if node.right.data == y:
                        temp[y] = node
                        print("temp : ", temp.get(y).data)
                    dq.appendleft(node.right)
                    # print("temp : ", temp.get(x), temp.get(y))
                    # print("temp : ", temp[x], temp[y])
            
                row.add(node.data)
            
            if x in row and y in row:
                print("in the same subtree")

                if temp[x] == temp[y]:
                    return False
                
                return True
            
        return False


       
    def inorder(self,temp):
        #temp=self.root
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)
            
    def mirrorImageInorder(self,node):
        if node:
            self.mirrorImageInorder(node.right)
            print(str(node.data))
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

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None

    def postOrderIterative(self, root):

        # Check for empty tree
        if root is None:
            return
        ans = list()
        stack = []

        while (True):

            while (root):
                # Push root's right child and then root to stack
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)

                # Set root as root's left child
                root = root.left

            # Pop an item from stack and set it as root
            root = stack.pop()

            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
            if (root.right is not None and
                    self.peek(stack) == root.right):
                stack.pop()  # Remove right child from stack
                stack.append(root)  # Push root back to stack
                root = root.right  # change root so that the
                # righ childis processed next

            # Else print root's data and set root as None
            else:
                ans.append(root.data)
                root = None

            if (len(stack) <= 0):
                break
        print(ans)


    def getHeight(self,temp):
        if temp:
            return 1 + max(self.getHeight(temp.left) ,self.getHeight(temp.right))
        else:
            return 0
        
    def minHeight(self, temp):
    
        if temp == None:
            return 0
    
        if temp.left == None and temp.right == None:
            return 1
    
        #First check whether node exist
        if temp.left is None:
            return 1 + self.minHeight(temp.right)
        
        if temp.right is None:
            return 1+self.minHeight(temp.left)
        
        return min(self.minHeight(temp.left), self.minHeight(temp.right)) + 1


    
    def getSize(self,temp):
        if temp:
            return 1+ self.getSize(temp.left) + self.getSize(temp.right)
        else:
            return 0
        
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
    
    
bst =Tree()        
#arr = [8,3,1,6,4,7,10,14,13,12,11,15,16,17,18,2,5,9]
arr=[4,5,3,6,5.5,6.5,2,7,1,8,9]
for item in arr:
    print(item)
    bst.createTree(item)

print("created bst")    
bst.inorder(bst.root)    
print("printed bst")    
bst.leftViewOfTree()    
bst.bfs() 

print("levelOrderTraversal :  ")
bst.breathFirstTravel()


print("bst.leftViewOfTree() : ")
bst.leftViewOfTree()
print("bst.rightViewOfTree() : ")
bst.rightViewOfTree()

print("bst.rightViewOfTree_trickySol() : ")
bst.rightViewOfTree()        
        
print('Inorder Traversal')
bst.inorder(bst.root) 
print('Preorder Traversal')
bst.preorder(bst.root) 
print('Postorder Traversal recursive')
bst.postorder(bst.root)
print('Postorder Traversal iteration')
bst.postOrderIterative(bst.root)


print('mirrorImageInorder')
bst.mirrorImageInorder(bst.root)


print("****************************height")
print(bst.getHeight(bst.root))


print("minHeight")
print(bst.minHeight(bst.root))


print("Size ")
print(bst.getSize(bst.root))

print("maxSumAtWhatLevel " )
bst.maxSumAtWhatLevel()

print("check is this modified tree is bst" )
print(bst.isBST(bst.root))

print ('Inorder Traversal')
bst.inorder(bst.root) 


print("bst.topView() : HAS SOME ISSUE   ?????")
#bst.topView()

print("bst.trimBst(tree,minVal,maxVal)")
#bst.trimBst()


print("finding val=5")
val=3
print(bst.findnode(bst.root,val))

print("is_cousin: **********")
# print(t1.is_cousin(6.5, 4.5))
# print(t1.is_cousin(3, 4))
print(t1.is_cousin(2, 6))
print(t1.is_cousin(2, 5.5))
# print(t1.is_cousin(1, 4.5))
# print(t1.is_cousin(0, 4.5))