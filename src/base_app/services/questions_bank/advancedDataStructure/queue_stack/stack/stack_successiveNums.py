import math

class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,val):
        self.items.append(val)
        
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("Stack is empty")
    
    def isEmpty(self):
        return self.items==[]

stack1=Stack()
for item in range(11):
    stack1.push(item)            

stack1.push(112)
#stack1.push(100)

stack2= Stack()

while not stack1.isEmpty():
    stack2.push(stack1.pop())
    
flag=True
while 1:
        
    try:
        item1=stack2.pop()
        item2=stack2.pop()
        
        if abs(item1 - item2) !=1:
            flag =False
            print(flag)
            break
    
    except:
        if flag == True:
            print("True")
        else:
            print("False")
        break
                