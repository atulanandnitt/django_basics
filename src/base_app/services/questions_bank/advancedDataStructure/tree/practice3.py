class Node:
    def __init__(self,val):
        self.data=val
        self.left =None
        self.right=None
        
    def __str__(self,val):
        return str(self.val)
    
class Tree:
    
    def __init__(self):
        self.root=None
    
    
    def createTree(self,val):
        if self.root is None:
            self.root = Node(val)
        
        else:
            tempNode = self.root
            while 1:
                if val < tempNode.data:
                    if tempNode.left:
                        tempNode = tempNode.left
                    else:
                        tempNode.left=Node(val)
                        return
                    
                if tempNode.data < val :
                    if tempNode.right:
                        tempNode = tempNode.right
                    else:
                        tempNode.right=Node(val)
                        return

    def inorder(self,tempNode):
        if tempNode:
            self.inorder(tempNode.left)
            print(tempNode.data)
            self.inorder(tempNode.right)

bst = Tree()
item=[4,5,3,7,1,8,2,9,11]

for items in item:
    bst.createTree(items)
    
bst.inorder(bst.root)    
            
                    
                    
        
    