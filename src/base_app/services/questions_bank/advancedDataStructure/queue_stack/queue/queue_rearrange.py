class Queue:
    def __init__(self):
        self.items=[]
    
    def enqueue(self,val):
        self.items.append(val)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        
    def isEmpty(self):
        return self.items ==[]
    
    def length(self):
        return len(self.items)
    
queue1=Queue()    
for item in range(10):
    queue1.enqueue(item)


queue2=Queue()
print(queue2.length())
l=queue2.length()
n=l//2
print("n :",l)

#while not queue1.isEmpty():
for i in range(n):
    val=queue1.dequeue()
    print(val)
    queue2.enqueue(val)

print(queue2.dequeue())
solQ=Queue()    
for i,j in range(n):
     solQ.enqueue(queue2.dequeue())
     solQ.enqueue(queue1.dequeue())
     
while not solQ.isEmpty():
    print(solQ.dequeue())