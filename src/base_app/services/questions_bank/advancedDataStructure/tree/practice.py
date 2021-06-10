class Node:
    def __init__(self,val):
        self.data = val
        self.leftChild=None
        self.rightChild=None
        
    def __str__(self):
        return str("str value is :"+ str(self.data))
    

class Tree:
    
    def __init__(self):
        self.root=None
    
    def addNode(self,val):
        if self.root:
            temp = self.root
            
            while 1:
                if val < temp.data:
                    if temp.leftChild:
                        temp=temp.leftChild
                    else:
                        temp.leftChild = Node(val)
                        break
                elif val > temp.data:
                    if temp.rightChild:
                        temp = temp.rightChild
                    else:
                        temp.rightChild = Node(val)
                        break
                else:
                    break
        else:
            self.root=Node(val)
        
    def getHeight(self,node):
        if node.leftChild and node.rightChild:
            return 1+ max(self.getHeight(node.leftChild),self.getHeight(node.rightChild))
        elif node.leftChild:
            return 1+ self.getHeight(node.leftChild)
        elif node.rightChild:
            return 1+ self.getHeight(node.rightChild)
        else:
            return 1
        a
    def getSize(self,node):
         if node.leftChild and node.rightChild:
             return 1+self.getSize(node.leftChild) + self.getSize(node.rightChild)
         elif node.leftChild:
             return 1+self.getSize(node.leftChild)
         elif node.rightChild:
             return 1+self.getSize(node.rightChild)
         else:
             return 1
         
        
    def inorder(self,node):
        if node:
            self.inorder(node.leftChild)
            print(str(node.data))
            self.inorder(node.rightChild)
            
    def preorder(self,node):
        if node:
            print(str(node))
            self.preorder(node.leftChild)
            self.preorder(node.rightChild)
            
    def postorder(self,node):
        if node:
            self.postorder(node.leftChild)
            self.postorder(node.rightChild)
            print(str(node))
            #print(self,type(self))
            
bst = Tree()
ar=[4,3,2,1,7,9]

for elem in ar:
    print("adding element",elem )
    bst.addNode(elem)            
            
print("bst in inorder")     
bst.inorder(bst.root)   
print("bst in preorder")
bst.preorder(bst.root)
print("bst in postorder")
bst.postorder(bst.root)

print("height of the tree is :")
print(bst.getHeight(bst.root))

print("size of the tree is :")
print(bst.getSize(bst.root))