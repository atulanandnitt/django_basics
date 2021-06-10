#bst

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        self.label=None
        
    
    def __str__(self):
        return str(self.val)
    
    
class Tree:
    
    def __init__(self):
        self.root = None
    
    def add_val(self,val):
        if self.root == None:
            self.root=Node(val)
        
        else:
            temp = self.root
            
            while 1:
                if val < temp.data:
                    if temp.left:
                        temp =temp.left
                    else:
                        temp.left=Node(val)
                        break
                elif val > temp.data:
                    if temp.right:
                        temp =temp.right
                    else:
                        temp.right=Node(val)
                        break
                else:
                    break

    def inorder(self,tempNode):
        if tempNode:
            self.inorder(tempNode.left)
            print(tempNode.data)
            self.inorder(tempNode.right)

    def getHeight(self,tempNode):
        if tempNode.left and tempNode.right:
            return (1 + max(self.getHeight(tempNode.left) , self.getHeight(tempNode.right) ))
        elif tempNode.left:
            return (1+ self.getHeight(tempNode.left))
        elif tempNode.right:
            return (1+ self.getHeight(tempNode.right))
        else:
            return 1
        
    def getSize(self,tempNode):
        if tempNode.left and tempNode.right:
            return 1+ self.getSize(tempNode.left) + self.getSize(tempNode.right)
        elif tempNode.left:
            return 1+self.getSize(tempNode.left)
        elif tempNode.right:
            return 1+self.getSize(tempNode.right)
        else:
            return 1
        
    def mirrorTreeInorder(self,tempNode):
        if tempNode:
            self.mirrorTreeInorder(tempNode.right)
            print(tempNode.data)
            self.mirrorTreeInorder(tempNode.left)
            
    queue =list()


    def bft(self): #Breadth-First Traversal

          self.root.level = 0 
          queue = [self.root]
          print("queue : ",queue,"type of queue",type(queue))
          out = []
          sumAtLevel = []
          temp_level = self.root.level

          while len(queue) > 0:
             #sumAtLevel =0    
             temp_node = queue.pop(0)
 
             if temp_node.level > temp_level:
                temp_level += 1
                out.append("\n")
                #sumAtLevel +=temp_node.data
                #print("sumAtLevel :" ,sumAtLevel)

             out.append(str(temp_node.data) + " ")
             print(out)
             sumAtLevel.append(temp_node.data)

             if temp_node.left:

                temp_node.left.level = temp_level + 1
                queue.append(temp_node.left)
                  

             if temp_node.right:

                temp_node.right.level = temp_level + 1
                queue.append(temp_node.right)
                      
               
          print ("".join(out))
          #print(out)
          #print("sumAtLevel :" ,sumAtLevel)
     
    """
    def countHalfNode(self,temp):
        #temp =self.root
        
        if((temp.left and !(temp.right)) or (temp.right and !(temp.left))):
            return 1
        
     """       
          
        
    def bft2(self):
         self.root.level =0
         queue=[self.root]
         out =[]
         temp_level=self.root.level
         
         while len(queue) >0:
             temp_node = queue.pop(0)
             
             if temp_node.level > temp_level:
                 temp_level +=1
                 out.append("\n")
             
             out.append(str(temp_node.data))
             print(out)
             
             if temp_node.left:
                 temp_node.left.level = temp_level +1
                 queue.append(temp_node.left)
                
             if temp_node.right:
                 temp_node.right.level = temp_level +1
                 queue.append(temp_node.right)
                 
             print ("".join(out))      
            
        
bst = Tree()

arr =[6,5,1,7]
queue =[1,2,3,4,5]
print(queue.pop(3))
rand_list = [3,4,2,5,6,1,8]
for item in rand_list:
    bst.add_val(item)     
    

#for item in arr:
    #bst.add_val(item)
    
bst.inorder(bst.root)

print("getHeight :", bst.getHeight(bst.root))

print("getSize :", bst.getSize(bst.root))

print("mirrorTreeInorder")
bst.mirrorTreeInorder(bst.root)

print ('Breadth-First Traversal')
bst.bft()

print ('Breadth-First Traversal : 2 ')
bst.bft2()

"""
a=[1,2,3,4,5]
print(len(a))
b="my name is atul"
print(len(b))
"""            