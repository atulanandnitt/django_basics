# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:32:19 2018

@author: atanand
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        #self.items.insert(0,item)
        self.items.append(item)

    def pop(self):
        #return self.items.pop(0)
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return len(self.items)

def iTop(infixexpr):
    print ("input:",infixexpr)
    prec = dict()#{}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    stackObject = Stack()
    postfixArray = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            print(token)
            postfixArray.append(token)
        else:
            print("stackObject : ",stackObject)
            while (not stackObject.isEmpty()) and \
               (prec[stackObject.peek()] >= prec[token]):
                  postfixArray.append(stackObject.pop())
            stackObject.push(token)

    while not stackObject.isEmpty():
        postfixArray.append(stackObject.pop())
    return " ".join(postfixArray)

myarray="A + B * C"
print(iTop(myarray))

myarray="A * B + C"
print(iTop(myarray))
