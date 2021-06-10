class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
    def __str__(self):
        return str(self.data)