

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
        if self.root is None:#if self.root == None:
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
    
#max depth
    def bft(self):
        def lastElementOfCurrentLevel(currentLeveElements):
            print("******currentLeveElements",currentLeveElements)
            lastElement=0
            while len(currentLeveElements)>0:
                lastElement= currentLeveElements.pop(0)
            return lastElement
        
        self.root.level=0
        temp_level= self.root.level
        queue=[self.root]
        result=[]
        currentLeveElements =[]
        SumcurrentLeveElements =0
        firstViewedFromLeft=[self.root.data]
        firstViewedFromRight=[]
        depth=0
        leftDepth,rightDepth=0,0
        while len(queue) >0:
            temp_node= queue.pop(0)
            print("queue ******************",queue)
            for item in queue:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",item)
            print("temp_node ******************",temp_node)
            print("temp_node.level ******************",temp_node.level)
            print( "temp_level ***********************",temp_level)
            
            if temp_node.level > temp_level:
                temp_level +=1
                result.append('\n')
                firstViewedFromLeft.append(temp_node.data)
                firstViewedFromRight.append(lastElementOfCurrentLevel(currentLeveElements))
                
                for item in currentLeveElements:
                    SumcurrentLeveElements += item
                print("SumcurrentLeveElements" ,SumcurrentLeveElements)
                SumcurrentLeveElements=0
                
                
                while len(currentLeveElements) >0:
                    currentLeveElements.pop(0)
            currentLeveElements.append(temp_node.data)            
            result.append((temp_node.data))#result.append(str(temp_node.data))
            print(result)
            
            print(result)
            for item in result:
                print(item)
            
            if temp_node.left:
                temp_node.left.level = temp_level+1
                leftDepth +=1
                queue.append(temp_node.left)
            
            if temp_node.right:
                temp_node.right.level = temp_level+1
                rightDepth +=1
                queue.append(temp_node.right)
        
        for item in currentLeveElements:
            SumcurrentLeveElements += item
        
        print(result)
        for item in result:
            print(item)
    
        print("SumcurrentLeveElements" ,SumcurrentLeveElements)
        #print("".join(result))
        print("firstViewedFromLeft",firstViewedFromLeft)
        firstViewedFromRight.append(lastElementOfCurrentLevel(currentLeveElements))
        print("firstViewedFromRight",firstViewedFromRight)
        depth=max(leftDepth,rightDepth)
        print("Depth is %%%%%%%%%%%%%%%",depth)
        
    
    def inorder(self,temp):
            
           if temp:
              
              self.inorder(temp.left)
              print (temp.data)#(str(node))
              self.inorder(temp.right)

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

    #bfs
    def maximum_difference_between_node_and_its_ancestor(self,root):
        tempQueue=[root]
        root.level=0
        tempLevel =0
        bstList=list()
        while len(tempQueue)>0:
            temp = tempQueue.pop(0)
            
            if temp.level > tempLevel:
                bstList.append('\n')
                tempLevel += 1
            
            bstList.append(temp.data)
            
            if temp.left:
                temp.left.level = temp.level +1
                tempQueue.append(temp.left)
            
            if temp.right:
                temp.right.level = temp.level +1
                tempQueue.append(temp.right)
                
        print(bstList)
                                
        




                       
tree = Tree()     
arr = [8,3,1,6,4,7]
for i in arr:
    tree.create(i)
print ('Breadth-First Traversal')
tree.bft()
print ('Inorder Traversal')
tree.inorder(tree.root) 
print ('Preorder Traversal')
tree.preorder(tree.root) 
print ('Postorder Traversal')
tree.postorder(tree.root)
print ('mirrorImageInorder')
tree.mirrorImageInorder(tree.root)

print("bst")
tree.maximum_difference_between_node_and_its_ancestor(tree.root)