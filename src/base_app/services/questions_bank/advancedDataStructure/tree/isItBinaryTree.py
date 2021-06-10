# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:13:28 2018

@author: atanand
"""

class Node:
    def __init__(self,val=None):
        self.left = None
        self.ight = None
        self.val = val
    
INFINITY = float('infinity')
NEG_INFINITY = float('-infinity')

def isBST(tree,minVal = NEG_INFINITY,maxVal = INFINITY):
    
    if tree is None:
        return True
    
    if not minVal <= tree.val <= maxVal:
        return False
    
    return isBST(tree.left,minVal,tree.val) and isBST(tree.right,tree.val,maxVal)

def isBST2(tree,lastNode =[NEG_INFINITY]):
    
    if tree is None:
        return True
    
    if not isBST2(tree.left,lastNode):
        return False
    
    if tree.val < lastNode[0]:
        return False
    
    lastNode[0] = tree.val
    
    return isBST2(tree.right,lastNode)

